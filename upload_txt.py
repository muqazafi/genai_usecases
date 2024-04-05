import streamlit as st
from adschatcontent import adscontent

# Define a function to process the file content
def process_file_content(file_content):
    # Split the file content into lines
    lines = file_content.split('\n')

    # Convert each line to uppercase
    output_lines = [line.upper() for line in lines]

    # Join the lines back together with newline characters
    output_text = '\n'.join(output_lines)

    return output_text

# Streamlit app
def get_file_txt():
#    st.title("File Content Processing App")

    # Get the file input from the user
    uploaded_file = st.file_uploader("Choose a Template file", type="txt")

    # Check if a file is uploaded
    if uploaded_file is not None:
        # Read the file content
        file_content = uploaded_file.read().decode("utf-8")

        # Process the file content
        output_text = process_file_content(file_content)
        adscontent(output_text)
        # Display the output
#        st.write("Output:")
#        st.code(output_text, language="txt")

#if __name__ == "__main__":
#    main()