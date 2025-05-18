import streamlit as st
from pyzbar.pyzbar import decode
from PIL import Image

def scan_qr_code(image):
    """
    Scans a QR code from an uploaded image and returns the decoded data.

    Args:
        image (UploadedFile): The uploaded image file.

    Returns:
        str or None: The decoded data from the QR code, or None if no QR code is found.
    """
    try:
        img = Image.open(image)
        decoded_objects = decode(img)

        if decoded_objects:
            # Assuming there's only one QR code in the image
            return decoded_objects[0].data.decode('utf-8')
        else:
            return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def main():
    st.title("QR Code Scanner")
    st.subheader("Upload an image containing a QR code")

    uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        st.write("Scanning QR code...")
        decoded_data = scan_qr_code(uploaded_file)

        if decoded_data:
            st.success("QR code successfully decoded!")
            st.write(f"Decoded data: **{decoded_data}**")
            if "github.com" in decoded_data:
                st.info(f"The decoded data appears to be a GitHub link: {decoded_data}")
                # You could add a button here to open the link if desired
                # if st.button("Open GitHub Link"):
                #     import webbrowser
                #     webbrowser.open_new_tab(decoded_data)
        else:
            st.warning("No QR code found in the uploaded image.")

if __name__ == "__main__":
    main()
