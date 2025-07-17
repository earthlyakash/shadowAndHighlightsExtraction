# 📌 Step 1: Install dependencies
!pip install opencv-python-headless pillow --quiet

# 📌 Step 2: Upload image
from google.colab import files
from PIL import Image
import numpy as np
import cv2
from IPython.display import display, Image as IPImage

uploaded = files.upload()
image_path = next(iter(uploaded))

# 📌 Step 3: Extract shadows and soft highlights
def extract_soft_shadow_highlight(image_path, highlight_start=200, highlight_end=255):
    # Load RGBA image
    pil_image = Image.open(image_path).convert("RGBA")
    np_image = np.array(pil_image)

    # Separate channels
    r, g, b, a = cv2.split(np_image)
    rgb = cv2.merge([r, g, b])
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY).astype(np.float32)
    alpha = a.astype(np.float32) / 255.0

    # Mask grayscale with alpha
    gray_alpha = gray * alpha
    norm_gray = cv2.normalize(gray_alpha, None, 0, 255, cv2.NORM_MINMAX)

    # --- Shadow ---
    shadow_alpha = (255 - norm_gray) * alpha
    shadow_alpha = np.clip(shadow_alpha, 0, 255).astype(np.uint8)

    # --- Highlight ---
    # Gradual transparency only for values > highlight_start
    highlight_mask = np.clip((norm_gray - highlight_start) / (highlight_end - highlight_start), 0, 1)
    highlight_alpha = (highlight_mask * 255 * alpha).astype(np.uint8)

    h, w = norm_gray.shape

    # Shadow image (black)
    shadow_result = np.zeros((h, w, 4), dtype=np.uint8)
    shadow_result[..., 3] = shadow_alpha

    # Highlight image (white)
    highlight_result = np.zeros((h, w, 4), dtype=np.uint8)
    highlight_result[..., 0:3] = 255
    highlight_result[..., 3] = highlight_alpha

    # Save files
    shadow_path = "gradual_shadow_output.png"
    highlight_path = "gradual_highlight_output.png"
    cv2.imwrite(shadow_path, cv2.cvtColor(shadow_result, cv2.COLOR_RGBA2BGRA))
    cv2.imwrite(highlight_path, cv2.cvtColor(highlight_result, cv2.COLOR_RGBA2BGRA))

    return shadow_path, highlight_path

# 📌 Step 4: Extract with smooth highlights
shadow_path, highlight_path = extract_soft_shadow_highlight(image_path, highlight_start=200, highlight_end=255)

# 📌 Step 5: Show results
print("🔻 Shadow Image (Smooth):")
display(IPImage(shadow_path))

print("🔺 Highlight Image (Gradual Alpha):")
display(IPImage(highlight_path))

# 📌 Step 6: Download files
files.download(shadow_path)
files.download(highlight_path)
