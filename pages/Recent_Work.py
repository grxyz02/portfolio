import streamlit as st
import base64
import hashlib

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
        </style>
        """,
        unsafe_allow_html=True
    )

# Add background image
add_background("image/bbb.png")

# Sidebar Cipher Selection
with st.sidebar:
    option = st.selectbox("Select a Cipher Method:", ["", "XOR Cipher", "Caesar Cipher","Hashing"])

# Main Content
if not option:
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
        Navigating the environment is a significant challenge for visually impaired individuals, as they often encounter obstacles
        and difficulties in identifying hazards. In response to this challenge, this study developed a SightStick prototype, 
        incorporating advanced technology to assist visually impaired individuals in obstacle avoidance.  
        """)
    else:
        st.header("🔍 **What’s This Project About?**")
        st.markdown("""
        ### 1️⃣ **BACKGROUND** 

        Navigating the environment presents a significant challenge for people with visual impairments, as they must continuously identify and avoid obstacles to move safely. With that, this study, proposes SightStick, a hybrid approach that 
        combines YOLOv8 and fuzzy logic to assist visually impaired individuals in navigating indoor environments

        ### 2️⃣ **OBJECTIVES**
        1. To develop a prototype that assists visually impaired individuals in navigating indoor
        environments.
        2. To integrate YOLOv8 and fuzzy logic algorithms in the developed prototype.
        3. To evaluate the performance of the SightStick prototype in the indoor environmen using:
            a. YOLOv8 in terms of mAP, Precision, Recall, and F1 score in classifying obstacles.
            b. Test Case Scenarios for the fuzzy logic algorithm in detecting obstacles.

        ### 3️⃣ **RESULTS**
        - This study, successfully developed the SightStick prototype, and was able to integrate sensors, cameras, and real-time data processing into a single device refer to figure 1. 
        """)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("image/pro.png", caption="Figure 1. SightStick Prototype", width=450)
    
        st.markdown("""
        - The SightStick prototype successfully integrated YOLOv8 object detection of and fuzzy logic for indoor navigation. It combined visual data with ultrasonic sensor distance measurements to detect obstacles and provide real-time navigation instructions. 

        - The researchers achieved a mean Average Precision (mAP) of 86.9% in obstacle classification using the YOLO algorithm, with an overall precision of 84.2%, a recall rate of 80.6%, and an F1-score of 82.36%.

        - The SightStick prototype showed strong performance in assisting visually impaired users with navigation, with a 72% success rate across 20 test cases. 
        """)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            youtube_url = "https://www.youtube.com/embed/c3MFq3UkDGg"
            st.markdown(
            f"""
            <div style="display: flex; justify-content: center;">
                <iframe width="640" height="360" 
                    src="{youtube_url}" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen>
                </iframe>
            </div>
            """,
            unsafe_allow_html=True,
        )

    
# Cipher Methods
if option == "XOR Cipher":
    st.header("XOR Cipher🗝️​🔐​")
    plaintext = st.text_area("Enter Plaintext:")
    key = st.text_input("Enter Key:")

    def xor_encrypt(plaintext, key):
        ciphertext = bytearray()
        for i in range(len(plaintext)):
            ciphertext.append(ord(plaintext[i]) ^ ord(key[i % len(key)]))
        return ciphertext

    def xor_decrypt(ciphertext, key):
        return xor_encrypt(ciphertext.decode(), key)  # XOR decryption is the same as encryption

    if st.button("Encrypt XOR"):
        if not plaintext or not key:
            st.error("Please provide both plaintext and key.")
        else:
            ciphertext = xor_encrypt(plaintext, key)
            st.success(f"Ciphertext: {ciphertext.decode(errors='replace')}")
            decrypted = xor_decrypt(ciphertext, key)
            st.info(f"Decrypted Text: {decrypted.decode()}")

elif option == "Caesar Cipher":
    st.header("Caesar Cipher🗝️​🔐​")

    def encrypt_decrypt(text, shift_keys, decrypt=False):
        result = ""
        for i, char in enumerate(text):
            shift = shift_keys[i % len(shift_keys)]
            if 32 <= ord(char) <= 125:
                new_ascii = ord(char) - shift if decrypt else ord(char) + shift
                while new_ascii > 125:
                    new_ascii -= 94
                while new_ascii < 32:
                    new_ascii += 94
                result += chr(new_ascii)
            else:
                result += char
        return result

    text = st.text_input("Enter Text:")
    shift_keys_str = st.text_input("Enter Shift Keys (space-separated):")
    
    if shift_keys_str:
        shift_keys = [int(key) for key in shift_keys_str.split()]
    else:
        shift_keys = []

    if st.button("Encrypt Caesar"):
        if not text or not shift_keys:
            st.error("Please provide both text and shift keys.")
        else:
            encrypted_text = encrypt_decrypt(text, shift_keys)
            st.success(f"Encrypted Text: {encrypted_text}")
            decrypted_text = encrypt_decrypt(encrypted_text, shift_keys, decrypt=True)
            st.info(f"Decrypted Text: {decrypted_text}")

elif option == "Hashing":
    st.header(" Hashing🗝️​🔐​")

    def hash_data(data, algorithm):
        if algorithm == "SHA-1":
            hash_value = hashlib.sha1(data.encode()).hexdigest().upper()
        elif algorithm == "SHA-256":
            hash_value = hashlib.sha256(data.encode()).hexdigest().upper()
        elif algorithm == "SHA-3":
            hash_value = hashlib.sha3_256(data.encode()).hexdigest().upper()
        elif algorithm == "MD5":
            hash_value = hashlib.md5(data.encode()).hexdigest().upper()
        else:
            return "Invalid algorithm"

        return hash_value

    # User input: text or file
    input_type = st.radio("Select input type:", ("Text", "File"))

    if input_type == "Text":
        text = st.text_area("Enter text:")
        algorithm = st.selectbox("Select hashing algorithm:", ("SHA-1", "SHA-256", "SHA-3", "MD5"))
        if st.button("Hash"):
            hash_value = hash_data(text, algorithm)
            st.write(f"{algorithm} hash:", hash_value)

    elif input_type == "File":
        file = st.file_uploader("Upload file:")
        if file is not None:
            file_contents = file.getvalue().decode("utf-8")
            algorithm = st.selectbox("Select hashing algorithm:", ("SHA-1", "SHA-256", "SHA-3", "MD5"))
            if st.button("Hash"):
                hash_value = hash_data(file_contents, algorithm)
                st.write(f"{algorithm} hash:", hash_value)

