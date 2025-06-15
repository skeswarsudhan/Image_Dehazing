# Image Dehazing Project

This project implements an image dehazing pipeline based on the paper:  
**"Efficient Image Dehazing with Boundary Constraint and Contextual Regularization" (Meng et al., ICCV 2013)**

---

## Project Overview

The dehazing process includes:

- **Airlight Estimation**  
- **Transmission Map Estimation**  
- **Transmission Refinement**  
- **Haze Removal**  
- **Image Quality Evaluation (PSNR, SSIM)**

---

## Files Description

### 1. `Airlight.py`

- Estimates the airlight (atmospheric light) from the hazy image.
- Uses minimum filtering approach with a configurable window size.

### 2. `CalTransmission.py`

- Calculates and refines the transmission map using contextual regularization.
- Applies a set of Kirsch filters and performs iterative optimization.

### 3. `removeHaze.py`

- Implements the dehazing formula to recover the haze-free image using airlight and transmission map.

### 4. `metrics.py`

- Computes PSNR and SSIM to evaluate image quality.
- Compares the dehazed image with reference (ground-truth) image.

### 5. `hazing.py`

- Generates synthetic hazy images by combining clean and smoke images.
- Resizes and overlays images to simulate haze effects.

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/skeswarsudhan/Image_Dehazing.git
cd <repository_folder>
```

### 2. Install dependencies
``` bash
pip install numpy opencv-python scikit-image matplotlib
```
(Install any additional packages if required)

### 3. Prepare Dataset
Provide your own dataset of clear and hazy images.

Update file paths inside the scripts as per your directory structure.

### 4. Run the Pipeline
Use hazing.py to create hazy images.

Run Airlight.py, CalTransmission.py, and removeHaze.py to perform dehazing.

Use metrics.py to compute evaluation metrics (PSNR, SSIM).

Folder Structure (Recommended)
```bash
project/
│
├── Airlight.py
├── CalTransmission.py
├── removeHaze.py
├── metrics.py
├── hazing.py
├── data/
│   ├── original/       # Original clean images
│   ├── haze/           # Generated hazy images
│   └── results/        # Dehazed results
└── README.md
```
### Notes
The implementation of Hazing is a novel approach discovered to calculate the amount of haze before and after removal. 

The Dehazing implementation is based directly on the ICCV 2013 dehazing paper.

Current code uses absolute paths — modify them to relative paths for portability.

Make sure image dimensions match when comparing for PSNR and SSIM.
