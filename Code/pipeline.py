"""
pipeline.py
Tích hợp pipeline từ 3 người
"""
import cv2
import imutils
from person1_preprocessing import ImagePreprocessor
from person2_detection import LicensePlateDetector
from person3_recognition import LicensePlateRecognizer
from config import IMAGE_WIDTH


class LicensePlatePipeline:
    """Pipeline hoàn chỉnh tích hợp 3 module"""

    def __init__(self):
        self.preprocessor = ImagePreprocessor()
        self.detector = LicensePlateDetector()
        self.recognizer = LicensePlateRecognizer()

    def process(self, image_path):
        """
        Xử lý toàn bộ pipeline

        Args:
            image_path: Đường dẫn ảnh

        Returns:
            dict: Kết quả đầy đủ
        """
        # Đọc ảnh
        img = cv2.imread(image_path)
        img = imutils.resize(img, width=IMAGE_WIDTH)

        # NGƯỜI 1: Tiền xử lý
        gray, thresh, steps = self.preprocessor.process(img)

        # NGƯỜI 2: Bắt biển số
        plate, info = self.detector.detect(gray, thresh)

        detection_visual = self.detector.get_detection_visual(img)

        # NGƯỜI 3: OCR
        text = self.recognizer.recognize(plate)
        ocr_image = self.recognizer.get_ocr_image()

        # Tổng hợp
        return {
            'text': text,
            'plate_image': plate,
            'plate_info': info,
            'processing_steps': {
                'blackhat': steps['blackhat'],
                'sobel': steps['sobel'],
                'threshold': steps['threshold'],
                'detection': detection_visual,
                'ocr': ocr_image
            },
            'original_image': img
        }


# Test pipeline
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python pipeline.py <image_path>")
        sys.exit(1)

    pipeline = LicensePlatePipeline()
    result = pipeline.process(sys.argv[1])

    print("\n" + "=" * 60)
    print("KẾT QUẢ PIPELINE")
    print("=" * 60)
    print(f"Biển số: {result['text']}")
    print(f"Loại xe: {result['plate_info']['type']}")
    print(f"Vị trí: ({result['plate_info']['x']}, {result['plate_info']['y']})")
    print(f"Kích thước: {result['plate_info']['w']}x{result['plate_info']['h']}")
    print("=" * 60)
