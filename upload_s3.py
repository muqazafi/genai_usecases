import streamlit as st
import boto3
import os
from QA import letschat
import json
from streamlit_extras.switch_page_button import switch_page

s3 = boto3.client('s3')
bucket_name='knowledge-base-s3-source'

def upload_to_s3(file, bucket_name):
    try:
        object_name = os.path.basename(file.name)
        s3.upload_fileobj(file, bucket_name, object_name)
        st.success(f"File '{object_name}' successfully uploaded ")
#        if st.button("Lets Chat"):
        letschat()
    except Exception as e:
        st.error(f"Error uploading file: {e}")

# Sidebar for user input


def get_file():
# Drag and drop file upload
        uploaded_files = st.file_uploader("Choose files or drag them here", type=["txt", "pdf", "jpg", "png"], accept_multiple_files=True)
        # Button to upload the files
        if uploaded_files is not None:
#            if st.button("Upload to S3"):
                for uploaded_file in uploaded_files:
                    upload_to_s3(uploaded_file, bucket_name)



def newline(result):    
    a = result
    i = 0
    ans = []                                 #list named ans for putting seperated words
    ans.append("")
    for x in range(len(a)):                  #iterating through the input
        if a[x] == "\\" and a[x+1] == "n":   #if it is "\n"
            a.replace("\n","  \n")
            i += 1
            ans.append("")
        elif (a[x-1] == "\\" and a[x] == "n"):
            pass
        else:
            ans[i] = ans[i] + a[x]
    for x in ans:
        return(ans) 