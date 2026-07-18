# CNN-Transformer Hybrid Model for Hairline Crack Detection

A hybrid deep learning model combining Convolutional Neural Networks (CNN) and Transformer architecture for detecting hairline cracks in structural surfaces.

## Project Structure

```
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
│   ├── model.py               # HybridCNNTransformer model definition
│   ├── predict.py             # Single image prediction (full)
│   ├── predict_simple.py      # Single image prediction (minimal)
│   └── train.py               # Training loop
└── outputs/                   # Results, plots, saved models
```

## Setup

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd CNN-TRANSFORMER-MODEL
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place your crack images in `data/raw/`.

## Usage

### Training

```bash
python src/train.py
```

### Prediction

```bash
python src/predict.py <image_path> --save_result --show --threshold 0.5
```

```bash
python src/predict_simple.py <image_path> --save_result
```

### Evaluation

```bash
python src/evaluate.py
```

## Documentation

Refer to the `docs/` folder for project abstract, site location details, and role summary.

## Status

**ONGOING**
