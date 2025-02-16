# 3D Model Viewer

## Overview
This project is a **web-based 3D model viewer** built using **Three.js**. It allows users to:
- **Switch between 3D models** stored in the `/static/` folder.
- **Upload their own `.glb` files** dynamically.
- **Orbit, zoom, and pan** around the models using mouse controls.

## Technologies Used
- **HTML, CSS, JavaScript** (Frontend)
- **Three.js** (3D Rendering)
- **Flask (Python)** (Backend for dynamic model listing)

---

## Features
✅ Load 3D `.glb` models dynamically from the `/static/` folder.  
✅ Allow users to upload and preview their own `.glb` files.  
✅ Easily switch between models with **Previous/Next** buttons.  
✅ Automatic **camera positioning** based on model size.  
✅ **Model scaling** to ensure visibility.  
✅ **Orbit controls** for easy model interaction.  

---

## Installation & Setup
### **1. Install Dependencies**  
Ensure you have **Python 3** installed. Then, install Flask:
```bash
pip install flask
```

After the download run the program using Windows Powershell and the following command:

```bash
python app.py
```
