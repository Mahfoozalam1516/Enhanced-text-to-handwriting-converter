# Enhanced Text to Handwriting Converter

This Streamlit app converts typed text into handwritten-style text with various customization options.

## Features

- Convert typed text to handwritten-style text
- Choose from multiple handwriting fonts
- Upload custom fonts
- Select background styles (Plain White, Lined Paper, Grid Paper)
- Upload custom background images
- Adjust font size, line height, and letter spacing
- Control handwriting randomness for a more natural look
- Download the generated handwritten text as an image

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/text-to-handwriting-converter.git
   cd text-to-handwriting-converter
   ```

2. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

4. Ensure you have the necessary font files in a `fonts` directory:
   - Caveat-Regular.ttf
   - IndieFlower-Regular.ttf
   - HomemadeApple-Regular.ttf
   - Handlee-Regular.ttf
   - Kalam-Regular.ttf

## Usage

1. Run the Streamlit app:

   ```
   streamlit run app.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually http://localhost:8501).

3. Enter your text in the text area.

4. Customize your handwriting:

   - Choose a handwriting style or upload your own font
   - Select a background style or upload your own image
   - Adjust font size, line height, and letter spacing
   - Set the handwriting randomness

5. Click "Convert to Handwriting" to generate your handwritten text.

6. Download the resulting image using the "Download Handwritten Image" button.

## Deploying on Streamlit

To deploy this app on Streamlit Sharing:

1. Push your code to a GitHub repository.

2. Go to [streamlit.io](https://streamlit.io/) and sign in with your GitHub account.

3. Create a new app and select your GitHub repository.

4. Streamlit will automatically detect the requirements.txt file and install the necessary dependencies.

5. Your app will be deployed and accessible via a unique URL.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
