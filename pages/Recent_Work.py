import streamlit as st
import base64

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
    option = st.selectbox("Select a Cipher Method:", ["", "XOR Cipher", "Caesar Cipher","Block Cipher"])

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

elif option == "Block Cipher":
    st.header(" Block Cipher🗝️​🔐​")


def pad(data, block_size):
    padding_length = block_size - len(data) % block_size  
    padding = bytes([padding_length] * padding_length)  
    return data + padding                         

def unpad(data):
    padding_length = data[-1]                                
    return data[:-padding_length]                           

def xor_encrypt_block(plaintext_block, key):
    encrypted_block = b''
    for i in range(len(plaintext_block)):
        encrypted_block += bytes([plaintext_block[i] ^ key[i % len(key)]])
    return encrypted_block                  

def xor_decrypt_block(ciphertext_block, key):
    return xor_encrypt_block(ciphertext_block, key)  

def xor_encrypt(plaintext, key, block_size):
    encrypted_data = b''
    padded_plaintext = pad(plaintext, block_size)
    
    st.markdown("### Encrypted Blocks", unsafe_allow_html=True)
    for x, i in enumerate(range(0, len(padded_plaintext), block_size)):
        plaintext_block = padded_plaintext[i:i+block_size]
        st.markdown(f"#### Plain block[{x}]:", unsafe_allow_html=True)
        st.markdown(f"<b>Hex:</b> {plaintext_block.hex()}", unsafe_allow_html=True)
        st.markdown(f"<b>Text:</b> {plaintext_block}", unsafe_allow_html=True)

        encrypted_block = xor_encrypt_block(plaintext_block, key)
        st.markdown(f"#### Cipher block[{x}]:", unsafe_allow_html=True)
        st.markdown(f"<b>Hex:</b> {encrypted_block.hex()}", unsafe_allow_html=True)
        st.markdown(f"<b>Text:</b> {encrypted_block}", unsafe_allow_html=True)
        
        encrypted_data += encrypted_block

    return encrypted_data                              

def xor_decrypt(ciphertext, key, block_size):
    decrypted_data = b''
    
    st.markdown("### Decrypted Blocks", unsafe_allow_html=True)
    for x, i in enumerate(range(0, len(ciphertext), block_size)):
        ciphertext_block = ciphertext[i:i+block_size]
        
        decrypted_block = xor_decrypt_block(ciphertext_block, key)
        
        st.markdown(f"#### Block[{x}]:", unsafe_allow_html=True)
        st.markdown(f"<b>Hex:</b> {decrypted_block.hex()}", unsafe_allow_html=True)
        st.markdown(f"<b>Text:</b> {decrypted_block}", unsafe_allow_html=True)
        
        decrypted_data += decrypted_block

    unpadded_decrypted_data = unpad(decrypted_data)
    
    return unpadded_decrypted_data                              

if __name__ == "__main__":
    plaintext_input = st.text_area("Plain Text:")
    key_input = st.text_input("Key:")
    block_size_input = st.text_input("Block Size:")
    submit_button = st.button("Submit")
    
    if submit_button:
        if not plaintext_input.strip() or not key_input.strip() or not block_size_input.strip():
            st.error("Please fill in all the fields.")
        else:
            plaintext = bytes(plaintext_input.encode())
            key = bytes(key_input.encode())
            try:
                block_size = int(block_size_input)
                if block_size not in [8, 16, 32, 64, 128]:
                    st.write('Block size must be one of 8, 16,  32, 64, or  128 bytes')
                else:
                    key = pad(key, block_size)
                    encrypted_data = xor_encrypt(plaintext, key, block_size)
                    decrypted_data = xor_decrypt(encrypted_data, key, block_size)
                    st.markdown("#### Original plaintext:", unsafe_allow_html=True)
                    st.code(plaintext)
                    st.markdown("#### Key byte:", unsafe_allow_html=True)
                    st.code(key)
                    st.markdown("#### Key hex:", unsafe_allow_html=True)
                    st.code(key.hex())
                    st.markdown("#### Encrypted data:", unsafe_allow_html=True)
                    st.code(encrypted_data.hex())
                    st.markdown("#### Decrypted data:", unsafe_allow_html=True)
                    st.code(decrypted_data.hex())
                    st.markdown("#### Decrypted data:", unsafe_allow_html=True)
                    st.code(decrypted_data)
            except ValueError:
                st.error("Please enter a valid integer for block size.")