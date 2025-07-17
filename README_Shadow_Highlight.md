
# 🌓 Shadow & Highlight Extractor with Transparency (Google Colab)

Extract smooth **shadows** and **highlights** from images (including PNGs with transparency) using Python — with full support for **gradual transparency**.  
This project is optimized to run in **Google Colab**, and allows users to upload images, process them, and download results.

---

## 🖼️ Features

- ✅ Supports images **with transparency (RGBA)**
- 🕶️ Extracts **soft shadows** (black with fading opacity)
- 🌞 Extracts **smooth highlights** (white with gradual transparency)
- 🧠 Uses grayscale + alpha to ensure realism
- 📥 Automatic **image upload** and **download buttons**
- ☁️ Ready to run in **Google Colab**

---

## 🔧 How It Works

1. User uploads an image (preferably PNG with transparency).
2. Code separates brightness into grayscale while respecting alpha transparency.
3. Shadow and highlight regions are extracted:
   - Shadows: dark areas turned black with fading alpha
   - Highlights: only very bright areas (e.g., 200–255) used with fading white overlay
4. Final outputs are saved and downloadable automatically.

---

## 🚀 Run It on Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)

Paste the code in Colab or upload the `.ipynb` if you have one.

---

## 🛠️ Requirements

These are installed automatically in Colab:

```bash
pip install opencv-python-headless pillow
```

---

## 📂 Output Files

- `gradual_shadow_output.png`: Soft black shadows with transparent background
- `gradual_highlight_output.png`: Smooth white highlights with gradual transparency

---

## 👤 Author

Created by **Akash Kumar**  
📧 [earthlyakash@gmail.com](mailto:earthlyakash@gmail.com)  
🆓 Free to use under MIT License

---

## 📸 Sample

Coming soon! You can upload your image and try it out.

