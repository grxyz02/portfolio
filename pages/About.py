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
        .skill-container {{
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }}
        .skill-label {{
            width: 150px;
            font-size: 16px;
            color: white;
        }}
        .skill-bar {{
            flex-grow: 1;
            background: #ddd;
            border-radius: 20px;
            overflow: hidden;
            height: 20px;
        }}
        .skill-bar-inner {{
            background: #00c3ff;
            height: 100%;
            line-height: 20px;
            color: white;
            text-align: right;
            padding-right: 10px;
            border-radius: 20px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add background image
add_background("image/bbb.png")

# About Section
st.title("About Me")
st.markdown(
    """
    <div style="
        border-left: 5px solid #00c3ff; 
        padding-left: 20px; 
        color: white; 
        font-size: 18px;
        text-align: left;
    ">
        <h4>About</h4>
        <p>
           As a dedicated and compassionate student with a good academic background, I am looking to start my career path and am enthusiastic about applying for technical support specialist. I’m a quick learner, and I view change and challenges as opportunities for personal and professional development. With my knowledge and capability, I  dedicate myself to contributing meaningful achievements as well as meeting the organization's objectives. 
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Skills Section with Labels and Progress Bars
st.markdown(
    """
    <div style="
        border-left: 5px solid #00c3ff; 
        padding-left: 20px; 
        color: white; 
        font-size: 18px;
        text-align: left;
    ">
        <h4>Skills</h4>
        <div class="skill-container">
            <div class="skill-label">Organized</div>
            <div class="skill-bar">
                <div class="skill-bar-inner" style="width: 90%;"></div>
            </div>
        </div>
        <div class="skill-container">
            <div class="skill-label">Communication</div>
            <div class="skill-bar">
                <div class="skill-bar-inner" style="width: 85%;"></div>
            </div>
        </div>
        <div class="skill-container">
            <div class="skill-label">Meeting Deadlines</div>
            <div class="skill-bar">
                <div class="skill-bar-inner" style="width: 80%;"></div>
            </div>
        </div>
        <div class="skill-container">
            <div class="skill-label">Critical Thinking</div>
            <div class="skill-bar">
                <div class="skill-bar-inner" style="width: 75%;"></div>
            </div>
        </div>
        <div class="skill-container">
            <div class="skill-label">Video Editing</div>
            <div class="skill-bar">
                <div class="skill-bar-inner" style="width: 70%;"></div>
            </div>
        </div>
        <div class="skill-container">
            <div class="skill-label">Programming</div>
            <div class="skill-bar">
                <div class="skill-bar-inner" style="width: 85%;"></div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="font-size: 18px; color: #333;">
        Click the button below to download my resume!
    </p>
    """,
    unsafe_allow_html=True
)

# Add a download button for the resume
#with open("resume.pdf", "rb") as file:
#    resume_data = file.read()

#st.download_button(
#    label="📄 Download Resume",
#    data=resume_data,
#    file_name="Grace_Torallo_Resume.pdf",
#    mime="application/pdf",
#)