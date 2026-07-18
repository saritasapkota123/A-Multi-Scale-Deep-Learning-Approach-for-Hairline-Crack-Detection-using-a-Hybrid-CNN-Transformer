import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import torch
from torchvision import transforms
from PIL import Image, ImageDraw, ImageFont
import argparse
from model import HybridCNNTransformer

parser = argparse.ArgumentParser(description="Simple Hairline Crack Detection")
parser.add_argument("img_path", type=str, help="Path to the image")
parser.add_argument("--save_result", action="store_true", help="Save image with prediction text")
parser.add_argument("--model", type=str, default="outputs/hybrid_model.pth", help="Path to saved model")
args = parser.parse_args()

# Load model
model = HybridCNNTransformer()
model.load_state_dict(torch.load(args.model, map_location=torch.device('cpu')))
model.eval()

# Preprocess image
image = Image.open(args.img_path).convert("RGB")
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])
input_tensor = transform(image).unsqueeze(0)

# Predict
with torch.no_grad():
    output = model(input_tensor)
    prob = torch.sigmoid(output).item()

print(f"Prediction Probability: {prob:.4f}")
if prob > 0.5:
    print("Hairline Crack Detected!")
    prediction_text = "Crack Detected"
else:
    print("No Crack Detected.")
    prediction_text = "No Crack"

# Optional: save image with prediction label
if args.save_result:
    original_image = Image.open(args.img_path).convert("RGB")
    draw = ImageDraw.Draw(original_image)

    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()

    draw.text((10, 10), f"{prediction_text} ({prob:.2f})", fill="red" if prob > 0.5 else "green", font=font)

    save_path = f"result_{os.path.basename(args.img_path)}"
    original_image.save(save_path)
    print(f"Result saved as: {save_path}")
