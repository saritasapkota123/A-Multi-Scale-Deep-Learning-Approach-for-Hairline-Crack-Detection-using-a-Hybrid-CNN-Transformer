# CrackFormer: A Multi-Scale CNN–Transformer Hybrid Model for Hairline Crack Detection

A hybrid deep learning framework for detecting hairline cracks (< 0.3 mm) in concrete structures, developed for structural health monitoring (SHM) applications. CrackFormer combines a multi-scale CNN backbone with a Swin Transformer and attention gates to jointly capture fine local crack texture and global crack continuity.

*Paper title:*
A Multi-Scale Deep Learning Approach for Hairline Crack Detection using a Hybrid CNN–Transformer Model

*Authors:*
- Sarita Sapkota¹ — Department of Civil Engineering, Kathmandu University
- Ravi Kumar Pajiyar² — Department of Computer Science & Engineering, Kathmandu University
- Prof. Dr. Sudan Jha² — Department of Computer Science & Engineering, Kathmandu University

---

## Abstract

Detecting hairline cracks — often less than 0.3 mm wide — is a critical but difficult task in structural health monitoring. These cracks are faint, easily lost in surface noise, and hard to segment accurately. CrackFormer addresses this by combining a multi-scale CNN, which captures fine local detail, with a Swin Transformer, which models the overall continuity of a crack even when it is broken or faint. Attention gates further help the model focus on crack features while suppressing distracting background patterns.

The model was evaluated on a combined dataset of SDNET2018, DeepCrack, and 1,200 original field images, achieving an *IoU of 85.4%* and an *F1-score of 92.1%*, outperforming baseline models such as U-Net and TransUNet by 3–5%. The paper also demonstrates how the model can be used to track crack growth over time, making it a practical tool for real-world infrastructure monitoring.

*Keywords:* Multi-scale deep learning · hairline crack detection · CNN–Transformer hybrid · crack evolution monitoring · structural health monitoring

---

## Motivation

The long-term health of concrete structures depends heavily on catching problems early, and hairline cracks are often the first visible sign of deterioration. Manual inspection is slow, subjective, and inconsistent — especially under difficult field conditions.

Existing deep learning approaches each fall short in a different way:
- *CNN-based models* (e.g., U-Net, DeepCrack) excel at local texture recognition but have a limited receptive field, making it hard to trace long, faint, or discontinuous cracks.
- *Transformer-based models* (e.g., Swin Transformer) capture global context well via self-attention, but tend to smooth over the fine boundary details needed for precise segmentation, and typically require large training datasets.

CrackFormer is designed to resolve this local-vs-global trade-off by combining both approaches in a single hybrid architecture.

## Model Architecture

- *Multi-scale CNN branch* — extracts fine-grained local crack texture and boundary detail across multiple resolutions.
- *Swin Transformer branch* — models long-range spatial dependencies to reconstruct broken or discontinuous crack paths.
- *Attention gates* — fuse CNN and Transformer features while suppressing background noise (surface texture, shadows, staining).

## Dataset

The model was trained and evaluated on a combined dataset consisting of:
- *SDNET2018* — public benchmark dataset for concrete crack classification.
- *DeepCrack* — public pixel-level crack segmentation dataset.
- *1,200 field images* — original images collected from concrete structures in Nepal, covering diverse surface types, finishes, lighting, and environmental conditions.

## Results

| Model | IoU | F1-score |
|---|---|---|
| U-Net | — | — |
| TransUNet | — | — |
| *CrackFormer (ours)* | *85.4%* | *92.1%* |

CrackFormer improves on U-Net and TransUNet baselines by 3–5% across evaluation metrics. The paper further demonstrates a crack-evolution tracking use case, showing how the model can monitor growth in crack length and width over time.

---

## Role of the First Author (Civil Engineering Perspective)

This project is an interdisciplinary collaboration between civil engineering and AI/computer science. As first author and the project's civil engineering researcher, Sarita Sapkota's contributions ensured that the model's design, data, and outputs remained grounded in real structural inspection practice:

- *Conceptualization & research design* — identified limitations of traditional crack detection methods and proposed the multi-scale hybrid deep learning approach, aligning the model's capabilities with real inspection needs.
- *Literature review* — reviewed conventional image-processing methods (Sobel, Canny, thresholding) and civil-engineering-based deep learning studies (e.g., Cha et al. 2017; SDNET2018; Zou et al. 2018) to identify research gaps.
- *Methodology & experimental setup* — designed the field data acquisition strategy across diverse concrete surfaces and conditions, and guided interpretation of multi-scale feature outputs in terms of crack morphology, orientation, and propagation.
- *Model validation (engineering accuracy)* — verified that predicted crack widths matched field measurements within acceptable tolerance, and assessed consistency across surface textures, finishes, and shadowing conditions.
- *Result interpretation* — translated quantitative metrics (IoU, F1, recall) into field-level reliability, focusing on micro-crack detection (< 0.3 mm), durability impact, and integration potential for drone- or camera-based inspection systems.
- *Drafting & editing* — authored the Introduction, Literature Review, civil-engineering sections of the Methodology, and Discussion, and contributed to refining the Abstract and Conclusion.

In short, this role served as the bridge between civil engineering principles and AI-based modeling, ensuring the hybrid CNN–Transformer model is both computationally sound and practically meaningful for structural condition assessment.

---

## Project Structure

CNN-TRANSFORMER-MODEL/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/                   # Crack images, site data
│   └── processed/             # Preprocessed/cleaned data
├── docs/
│   ├── Abstract_and_Introduction.pdf
│   ├── Site_location.pdf
│   └── Role_Summary_Civil_Engineering.pdf
├── notebooks/                 # Exploratory Jupyter notebooks
├── src/
│   ├── data.py                # Data loading and preprocessing
│   ├── evaluate.py            # Model evaluation scripts
│   ├── model.py                # HybridCNNTransformer model definition
│   ├── predict.py             # Single image prediction (full)
│   ├── predict_simple.py      # Single image prediction (minimal)
│   └── train.py               # Training loop
└── outputs/                   # Results, plots, saved models

## Setup

1. Clone the repository:
   
   git clone <repo-url>
   cd CNN-TRANSFORMER-MODEL
   

2. Install dependencies:
   
   pip install -r requirements.txt
   

3. Place your crack images in data/raw/.

## Usage

### Training

python src/train.py

### Prediction

python src/predict.py <image_path> --save_result --show --threshold 0.5

python src/predict_simple.py <image_path> --save_result

### Evaluation

python src/evaluate.py

## Documentation

See the docs/ folder for the project abstract and introduction, site location details, and the first author's role summary.

## References

1. O. Ronneberger, P. Fischer, and T. Brox, "U-Net: Convolutional Networks for Biomedical Image Segmentation," MICCAI, pp. 234–241, 2015.
2. Q. Zou et al., "DeepCrack: Learning Hierarchical Feature Representations for Crack Detection," IEEE IPAS, 2018, pp. 1–6.
3. Z. Liu et al., "Swin Transformer: Hierarchical Vision Transformer Using Shifted Windows," ICCV, 2021, pp. 10012–10022.

## Status

*ONGOING*
