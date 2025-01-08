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
        .info-box {{
            display: inline-block;
            background: linear-gradient(to right, #d4edda 50%, #ffffff 50%);
            border: 1px solid #c3e6cb;
            padding: 10px;
            border-radius: 5px;
            color:rgb(3, 80, 21);
            font-size: 16px;
            font-family: Arial, sans-serif;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add background image
add_background("image/b.png")

# Content with a left border
st.markdown(
    """
    <div style="
        border-left: 5px solid #00c3ff; 
        padding-left: 20px; 
        color: white; 
        font-size: 18px;
        text-align: left;
    ">
        <h1>Hi, I'm Grace 🤖</h1>
        <p>
          Start browsing to discover the perfect blend of <br> passion,
          creativity, and dedication. Whether you're <br> here to explore
          my skills, achievements, or future <br> potential, you're in for
          a treat. Dive in—because <br> great things start with curiosity! 👩‍💻
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Add a custom half-highlighted info box with border equal to text length
st.markdown(
    """
    <div class="info-box">
        Use the sidebar to navigate!
    </div>
    """,
    unsafe_allow_html=True
)

# Contact Information Section
st.markdown(
    """
    <div style="font-size: 16px; margin-top: 70px; color: white;">
        📞 09515683359 <br>
        📧 torallograyce@gmail.com <br>
        📍 Del Rosario Banao, Iriga City
    </div>
    """,
    unsafe_allow_html=True
)
