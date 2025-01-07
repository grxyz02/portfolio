import streamlit as st

st.set_page_config(page_title="learn gpt", page_icon="🗃️")

# Add custom CSS for the background image
def add_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url({image_url});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function and pass the image URL or local path
add_background("image/1.png")

# Your Streamlit app content
st.title("Streamlit App with Background Image")
st.write("This app has a custom background image!")