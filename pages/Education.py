import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="Learn GPT", page_icon="🤖", layout="wide")

# Function to add a background image
def add_background(image_path):
    with open(image_path, "rb") as image_file:
        # Encode the image as Base64
        encoded_string = base64.b64encode(image_file.read()).decode()
    # Inject the CSS with the Base64-encoded image
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        h4 {{
            margin-top: 10px;
            margin-bottom: 5px;
            color: #00c3ff;
        }}
        p {{
            color: white;
            font-size: 16px;
            margin-bottom: 20px;
        }}
        .section {{
            border-left: 5px solid #00c3ff;
            padding-left: 15px;
            margin-bottom: 20px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add background image
add_background("image/bbb.png")

# Title
st.title("Education")

# Split the content into two columns
col1, col2 = st.columns(2)

# Left Column: Tertiary and Senior High School
with col1:
    st.markdown(
        """
        <div class="section">
            <h4>Tertiary</h4>
            <p>
                Camarines Sur Polytechnic Colleges <br>
                Bachelor of Science in Computer Science <br>
                San Miguel, Nabua, Camarines Sur<br>
                Dean Lister<br>
                2021 - 2025<br>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="section">
            <h4>Junior High School</h4>
            <p>
                Rinconada National Technical Vocational School <br>
                Sto. Domingo, Iriga City, Camarines Sur<br>
                With High Honors<br>
                2016 - 2019<br>
            </p>
        </div>

        """,
        unsafe_allow_html=True,
    )

# Right Column: Junior High School and Elementary
with col2:
    st.markdown(
        """
        <div class="section">
            <h4>Senior High School</h4>
            <p>
                Rinconada National Technical Vocational School <br>
                TVL Track - FPP & BPP<br>
                Sto. Domingo, Iriga City, Camarines Sur<br>
                With High Honors<br>
                2019 - 2021<br>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="section">
            <h4>Elementary</h4>
            <p>
                Banao Elementary School <br>
                Del Rosario Banao, Iriga City, Camarines Sur<br>
                With Honors<br>
                2009 - 2016<br>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
