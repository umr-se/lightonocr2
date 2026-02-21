import sys
import torch
from PIL import Image
from transformers import LightOnOcrForConditionalGeneration, LightOnOcrProcessor

MODEL_PATH = r"models\LightOnOCR-2-1B"
MAX_NEW_TOKENS = 200

device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.bfloat16 if device == "cuda" else torch.float32

model = LightOnOcrForConditionalGeneration.from_pretrained(
    MODEL_PATH,
    torch_dtype=dtype,
    local_files_only=True
).to(device).eval()

processor = LightOnOcrProcessor.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)


def run_ocr(image_path, output_file="output.txt"):
    try:
        image = Image.open(image_path).convert("RGB")
        max_size = 1024
        if max(image.size) > max_size:
            image.thumbnail((max_size, max_size))
    except Exception as e:
        print("Failed to open image:", e)
        return

    conversation = [
        {"role": "user", "content": [{"type": "image", "image": image}]}
    ]

    inputs = processor.apply_chat_template(
        conversation,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    )

    inputs = {
        k: v.to(device, dtype=dtype) if v.is_floating_point() else v.to(device)
        for k, v in inputs.items()
    }

    with torch.inference_mode():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=MAX_NEW_TOKENS,
            do_sample=False
        )

    generated = output_ids[0, inputs["input_ids"].shape[1]:]
    text = processor.decode(generated, skip_special_tokens=True)

    print("OCR Result:\n")
    print(text)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"\nText saved to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_ocr(sys.argv[1])
    else:
        path = input("Enter image path: ").strip()
        if path:
            run_ocr(path)
        else:
            print("No image provided.")
