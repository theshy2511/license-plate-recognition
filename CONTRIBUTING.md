# Contributing to Vietnamese License Plate Recognition System

Thank you for your interest in contributing to this project! 🎉

## 🚀 How to Contribute

### 1. Fork the Repository

Click the "Fork" button at the top right of this page.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/license-plate-recognition.git
cd license-plate-recognition
```

### 3. Create a Branch

```bash
git checkout -b feature/YourFeatureName
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring

### 4. Make Your Changes

- Write clean, readable code
- Follow PEP 8 style guide
- Add docstrings to functions
- Comment complex logic
- Test your changes

### 5. Commit Your Changes

```bash
git add .
git commit -m "Add: Brief description of your changes"
```

Commit message format:
- `Add:` - New features
- `Fix:` - Bug fixes
- `Update:` - Updates to existing features
- `Refactor:` - Code refactoring
- `Docs:` - Documentation changes

### 6. Push to Your Fork

```bash
git push origin feature/YourFeatureName
```

### 7. Create a Pull Request

- Go to the original repository
- Click "New Pull Request"
- Select your branch
- Describe your changes
- Submit!

## 📝 Code Style Guidelines

### Python Style

Follow PEP 8:
```python
# Good
def detect_license_plate(image, threshold=0.5):
    """
    Detect license plate in the image.

    Args:
        image: Input image (numpy array)
        threshold: Detection confidence threshold

    Returns:
        Detected plate region or None
    """
    pass

# Bad
def detectPlate(img,th=0.5):
    pass
```

### Naming Conventions

- **Variables:** `snake_case`
- **Functions:** `snake_case`
- **Classes:** `PascalCase`
- **Constants:** `UPPER_SNAKE_CASE`

### Docstrings

Use Google-style docstrings:
```python
def process_image(image_path, config=None):
    """
    Process image through the recognition pipeline.

    Args:
        image_path (str): Path to input image
        config (dict, optional): Configuration parameters

    Returns:
        dict: Recognition results with keys:
            - text: Recognized license plate text
            - confidence: Recognition confidence score
            - plate_image: Cropped plate region

    Raises:
        FileNotFoundError: If image_path doesn't exist
        ValueError: If image format is unsupported
    """
    pass
```

## 🧪 Testing

Before submitting:

1. **Test your code:**
   ```bash
   python main.py
   ```

2. **Test on different images:**
   - Old motorcycle plates
   - New motorcycle plates
   - Car plates
   - Poor lighting conditions

3. **Check for errors:**
   - No runtime errors
   - No warnings
   - Handles edge cases

## 🐛 Reporting Bugs

Create an issue with:

**Title:** Brief, descriptive title

**Description:**
- What happened?
- What did you expect?
- Steps to reproduce
- Screenshots (if applicable)

**Environment:**
- OS: Windows 10 / Ubuntu 20.04 / macOS 12
- Python version: 3.8 / 3.9 / 3.10
- Dependencies versions

**Example:**
```
Title: Detection fails on motorcycle plates with new format

Description:
When processing images with new motorcycle plates (5-digit format),
the detection module fails to locate the plate region.

Steps to reproduce:
1. Load image: Dataset/xe_may/bien_moi/60B8_010.75.jpg
2. Click "Nhận dạng"
3. Error appears: "No plate detected"

Expected: Should detect plate region

Environment:
- OS: Windows 10
- Python: 3.9.7
- OpenCV: 4.8.0
```

## 💡 Feature Requests

We welcome suggestions! Create an issue with:

- **Feature description:** What do you want?
- **Use case:** Why is it useful?
- **Possible implementation:** Ideas on how to implement

## 📋 Pull Request Checklist

Before submitting PR, ensure:

- [ ] Code follows PEP 8 style guide
- [ ] Added docstrings to new functions
- [ ] Tested on multiple images
- [ ] No new warnings or errors
- [ ] Updated README.md (if needed)
- [ ] Added comments to complex code
- [ ] Branch is up to date with main

## 🏆 Recognition

Contributors will be added to the Acknowledgments section in README.md!

## 📞 Questions?

Open an issue with the "question" label or contact the maintainer.

---

Thank you for contributing! 🙏
