"""
person3_recognition.py
Module nhận dạng ký tự - NGƯỜI 3 (Phần B)
ĐÃ TỐI ƯU: Giữ nguyên text gốc từ PaddleOCR, không format lại
"""

import os
os.environ['FLAGS_logtostderr'] = '0'
os.environ['GLOG_minloglevel'] = '2'

import cv2
import numpy as np
from paddleocr import PaddleOCR

class LicensePlateRecognizer:
    def __init__(self):
        print("🔄 Đang khởi tạo PaddleOCR...")
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en')
        self.ocr_image = None
        self.raw_text = None
        print("✅ PaddleOCR đã sẵn sàng!")

    def recognize(self, plate_image):
        """Nhận dạng text từ biển số - GIỮ NGUYÊN FORMAT GỐC"""
        if plate_image is None or not isinstance(plate_image, np.ndarray):
            return "Không nhận dạng được"

        try:
            # ✅ BƯỚC 1: Tạo gray TRƯỚC
            if len(plate_image.shape) == 2:
                gray = plate_image  # ← Khai báo gray ở đây
                plate_bgr = cv2.cvtColor(plate_image, cv2.COLOR_GRAY2BGR)
            else:
                gray = cv2.cvtColor(plate_image, cv2.COLOR_BGR2GRAY)  # ← Khai báo gray
                plate_bgr = plate_image.copy()

            self.ocr_image = plate_bgr.copy()

            # ✅ BƯỚC 2: Tạo binary image (SAU KHI ĐÃ CÓ gray)
            _, self.binary_image = cv2.threshold(
                gray, 0, 255,
                cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )

            # Resize nếu quá nhỏ
            h, w = plate_bgr.shape[:2]
            if h < 60:
                scale = 60 / h
                new_w = int(w * scale)
                plate_bgr = cv2.resize(plate_bgr, (new_w, 60),
                                       interpolation=cv2.INTER_CUBIC)

            # PaddleOCR
            result = self.ocr.ocr(plate_bgr)

            if not result:
                return "Không nhận dạng được"

            # ✅ THAY ĐỔI: Lấy text và GIỮ NGUYÊN format
            texts = []
            for page in result:
                if isinstance(page, dict):
                    if 'rec_texts' in page and 'rec_scores' in page:
                        texts.extend(page['rec_texts'])
                        print(f"🔍 Phát hiện {len(page['rec_texts'])} text:")
                        for text, score in zip(page['rec_texts'], page['rec_scores']):
                            print(f"  - '{text}' (tin cậy: {score:.2f})")

                elif isinstance(page, list):
                    for line in page:
                        texts.append(line[1][0])
                        print(f"  - '{line[1][0]}' (tin cậy: {line[1][1]:.2f})")

            if not texts:
                return "Không nhận dạng được"

            full_text = "\n".join(texts)

            print(f"📝 Raw text: {repr(full_text)}")

            # ✅ CHỈ LÀM SẠCH ký tự lạ, KHÔNG FORMAT LẠI
            cleaned = self._clean_text_only(full_text)

            print(f"✅ Kết quả cuối: '{cleaned}'")

            if len(cleaned.replace('\n', '').replace(' ', '')) < 6:
                return "Không nhận dạng được"

            self.recognized_text = cleaned
            return cleaned

        except Exception as e:
            print(f"❌ Lỗi PaddleOCR: {e}")
            import traceback
            traceback.print_exc()
            return "Không nhận dạng được"

    def _clean_text_only(self, text):

        # Cho phép: chữ, số, dấu gạch ngang, chấm, xuống dòng
        allowed_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.\n ')

        cleaned = ""
        for c in text.upper():
            if c in allowed_chars:
                cleaned += c

        cleaned = cleaned.strip()

        return cleaned

    def get_ocr_image(self):
        if self.ocr_image is None:
            return np.zeros((60, 200, 3), dtype=np.uint8)
        return self.ocr_image

    def get_binary_image(self):
        if self.binary_image is None:
            return np.zeros((60, 200), dtype=np.uint8)
        return self.binary_image