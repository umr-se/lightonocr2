# LightOnOCR Image-to-Text Script

This project provides a simple command-line OCR pipeline built with **PyTorch**, **Transformers**, and the LightOnOCR model. It allows you to extract text from images locally using GPU acceleration (if available) and save the results to a text file.

The script loads the model from a local directory and performs inference on a provided image, resizing it if needed to improve performance.

---

## Features

* Runs fully offline using locally stored model weights
* Automatic GPU detection (falls back to CPU if unavailable)
* Image resizing for large inputs
* Saves OCR output to a text file
* Simple command-line usage

---

## Requirements

Make sure you have Python 3.9+ installed.

Install dependencies:

```bash
pip install torch pillow transformers
```

This project relies on:

* PyTorch for model inference
* Hugging Face Transformers for model loading and processing
* PIL for image handling

---

## Model Download

Download the LightOnOCR-2 model from Hugging Face and place it in:

```
models/LightOnOCR-2-1B
```

Model page:
https://huggingface.co/lightonai/LightOnOCR-2-1B

---

## Project Structure

```
project/
│
├── models/
│   └── LightOnOCR-2-1B/
│
├── ocr_script.py
└── README.md
```

---

## Usage

### Run with image path argument

```bash
python ocr_script.py sample.png
```

### Or run interactively

```bash
python image.py
```

You will be prompted to enter the image path.

---

## How It Works

1. Loads the LightOnOCR model from disk
2. Opens the image and converts it to RGB
3. Resizes image if larger than 1024px
4. Sends it through the OCR model
5. Prints extracted text
6. Saves output to `output.txt`

---

## Configuration

You can edit these values in the script:

```python
MODEL_PATH = r"models\LightOnOCR-2-1B"
MAX_NEW_TOKENS = 200
```

* **MODEL_PATH** → location of downloaded model
* **MAX_NEW_TOKENS** → maximum OCR output length

---

## GPU Support

The script automatically selects:

* CUDA GPU if available
* Otherwise CPU

For best performance, use a GPU with at least **8GB VRAM**.

---

## Output

The extracted text is:

* Printed in the console
* Saved to `output.txt` (or custom filename)

---

## Results
![test](https://github.com/user-attachments/assets/2ff4ba84-329f-49c8-a0e0-c878e586906f)
[output.txt](https://github.com/user-attachments/files/25456477/output.txt)

---

## License

Check the Hugging Face model page for license information before commercial use.

---

## Credits

* LightOnAI for the OCR model
* Hugging Face for hosting and tooling
