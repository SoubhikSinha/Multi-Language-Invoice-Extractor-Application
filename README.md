# Multi-Language Invoice Extractor Application (Google Gemini)

## Acknowledgement

[](https://github.com/SoubhikSinha/Text-Summarization-LangChain#acknowledgement)

I would like to extend my sincere thanks to  [Krish Naik](https://github.com/krishnaik06)  for his invaluable content and guidance, which helped me build this project. This project wouldn't have been possible without his educational resources.

<br>
 
## About the Project
his project focuses on developing a Streamlit-based **Multi-Language Invoice Extractor Application** utilizing [Google Gemini](https://ai.google.dev/gemini-api/docs/models/gemini) for advanced image-to-text processing and natural language understanding. The application allows users to upload an invoice image in **any language**, where **[OCR (Optical Character Recognition)](https://cloud.google.com/use-cases/ocr)** extracts textual content from the invoice. Leveraging **Google Gemini's** multimodal capabilities, the extracted text is processed to enable users to ask **custom queries**, retrieving relevant details dynamically based on the uploaded invoice's content. The application features **multi-language support**, **AI-powered question answering**, and an intuitive **Streamlit UI**, ensuring seamless interaction. By integrating **OCR** for accurate text extraction and the **Google Gemini API** for contextual understanding, this tool streamlines invoice data processing, making it efficient and adaptable for diverse linguistic and document-processing needs.

<br>

## How to Run the Project ?

### **1. Clone the Repository**
Clone the repository to your local machine :
```bash
git clone https://github.com/SoubhikSinha/Multi-Language-Invoice-Extractor-Application.git
```
  
<br>

### **2. Create a Virtual Environment**
Navigate to the repository's root directory and create a Conda virtual environment :
```bash
conda create --prefix ./venv python=3.11 -y
```

<br>

### **3. Activate the Conda Environment**
Activate the newly created environment :
```bash
conda activate venv/
```

<br>

### **4. Install Required Libraries**
Install all the necessary dependencies :
```bash
pip install -r requirements.txt
```

<br>

### **5. Set Up Google API Key**
Create and paste your Google API key inside `.env` file. Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

Example `.env` file content :
```bash
GOOGLE_API_KEY="your_api_key_here"
```

<br>

### **6. Run the Application**
Start the Streamlit application by running :
```bash
streamlit run app.py
```

<br>

### **7. Play Around!**
Explore the features of the Multi-Language Invoice Extractor Application and enjoy!

