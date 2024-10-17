import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import random
import os

# Assume these font files are in a 'fonts' directory
FONT_PATHS = {
    "Caveat": "fonts/Caveat-Regular.ttf",
    "Indie Flower": "fonts/IndieFlower-Regular.ttf",
    "Homemade Apple": "fonts/HomemadeApple-Regular.ttf",
    "Handlee": "fonts/Handlee-Regular.ttf",
    "Kalam": "fonts/Kalam-Regular.ttf"
}

def get_handwriting_font(font_name, font_size=30):
    if font_name == "Custom":
        return ImageFont.truetype(io.BytesIO(st.session_state.custom_font), font_size)
    font_path = FONT_PATHS.get(font_name, FONT_PATHS["Caveat"])
    return ImageFont.truetype(font_path, font_size)

def create_background(width, height, texture):
    if texture == "Custom":
        custom_bg = Image.open(io.BytesIO(st.session_state.custom_background))
        return custom_bg.resize((width, height))
    elif texture == "Plain White":
        return Image.new('RGB', (width, height), color='white')
    elif texture == "Lined Paper":
        img = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(img)
        for y in range(0, height, 25):
            draw.line([(0, y), (width, y)], fill='lightblue', width=1)
        draw.line([(40, 0), (40, height)], fill='pink', width=1)
        return img
    elif texture == "Grid Paper":
        img = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(img)
        for x in range(0, width, 25):
            draw.line([(x, 0), (x, height)], fill='lightblue', width=1)
        for y in range(0, height, 25):
            draw.line([(0, y), (width, y)], fill='lightblue', width=1)
        return img

def get_text_dimensions(text, font):
    ascent, descent = font.getmetrics()
    bbox = font.getmask(text).getbbox()
    if bbox is None:
        return (font.size, font.size)  # Return default size for whitespace
    text_width = bbox[2]
    text_height = bbox[3] + descent
    return (text_width, text_height)

def text_to_handwriting(text, font, line_height, letter_spacing, randomness):
    lines = text.split('\n')
    max_line_width = max(sum(get_text_dimensions(char, font)[0] for char in line) for line in lines)
    total_height = len(lines) * line_height

    padding = 50
    img_width = max_line_width + (2 * padding) + (len(max(lines, key=len)) * letter_spacing)
    img_height = total_height + (2 * padding)
    
    img = create_background(img_width, img_height, st.session_state.background)
    draw = ImageDraw.Draw(img)

    y = padding
    for line in lines:
        x = padding
        for char in line:
            rand_x = random.uniform(-randomness, randomness)
            rand_y = random.uniform(-randomness, randomness)
            draw.text((x + rand_x, y + rand_y), char, font=font, fill='black')
            char_width, _ = get_text_dimensions(char, font)
            x += char_width + letter_spacing
        y += line_height

    return img

def main():
    st.title("Enhanced Text to Handwriting Converter")

    if 'background' not in st.session_state:
        st.session_state.background = "Plain White"
    if 'custom_font' not in st.session_state:
        st.session_state.custom_font = None
    if 'custom_background' not in st.session_state:
        st.session_state.custom_background = None

    user_text = st.text_area("Enter your text here:", height=200)

    col1, col2 = st.columns(2)
    with col1:
        font_option = st.selectbox(
            "Choose a handwriting style:",
            ["Custom"] + list(FONT_PATHS.keys())
        )
        if font_option == "Custom":
            uploaded_font = st.file_uploader("Upload your own font file (TTF format)", type="ttf")
            if uploaded_font:
                st.session_state.custom_font = uploaded_font.read()

    with col2:
        background_option = st.selectbox(
            "Choose a background style:",
            ["Custom", "Plain White", "Lined Paper", "Grid Paper"]
        )
        if background_option == "Custom":
            uploaded_bg = st.file_uploader("Upload your own background image", type=["png", "jpg", "jpeg"])
            if uploaded_bg:
                st.session_state.custom_background = uploaded_bg.read()
    
    st.session_state.background = background_option

    col1, col2, col3 = st.columns(3)
    with col1:
        font_size = st.slider("Font Size", 20, 50, 30)
    with col2:
        line_height = st.slider("Line Height", 30, 100, 60)
    with col3:
        letter_spacing = st.slider("Letter Spacing", 0, 20, 5)

    randomness = st.slider("Handwriting Randomness", 0.0, 5.0, 2.0)

    if st.button("Convert to Handwriting"):
        if user_text:
            try:
                font = get_handwriting_font(font_option, font_size)
                result_image = text_to_handwriting(user_text, font, line_height, letter_spacing, randomness)

                buf = io.BytesIO()
                result_image.save(buf, format="PNG")
                byte_im = buf.getvalue()

                st.image(byte_im, caption="Your text in handwriting", use_column_width=True)

                st.download_button(
                    label="Download Handwritten Image",
                    data=byte_im,
                    file_name="handwritten_text.png",
                    mime="image/png"
                )
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter some text to convert.")

if __name__ == "__main__":
    main()