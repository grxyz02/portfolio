import streamlit as st
import base64

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

        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add background image
add_background("image/bbb.png")
st.title("📊 **Recent Work**")

# Checkbox for Text-Only Mode
show_text_only = st.checkbox("View Text Only")

if show_text_only:

    st.write("""
    🌟 **SightStick: A Hybrid Approach for Visually Impaired Individuals Using YOLO and Fuzzy Logic Algorithm** 🌟
             
             **📝Author**: 
            
            Caritos, Alyssa P.
            Dimanarig, Shiella R.
            Torallo, Gracia P.

    
    ### 🔍 **What’s This Project About?**  
    This project is all about **building models** and **running simulations** using Python. By generating synthetic data and leveraging Python’s rich ecosystem of libraries, we will:  
    - 🛠️ Explore how to analyze and simulate real-world scenarios.  
    - 📊 Build statistical models and evaluate their behavior.  
    - 🔄 Apply these techniques to gain deeper insights into systems and processes.  
    """)
else:
    # Introduction Section
    st.header("🔍 **What’s This Project About?**")
    st.markdown("""
    This project is all about **building models** and **running simulations** using Python.  
    By generating synthetic data and leveraging Python’s rich libraries, we will:  
    - 🛠️ Explore how to analyze and simulate real-world scenarios.  
    - 📊 Build statistical models and evaluate their behavior.   
    """)
