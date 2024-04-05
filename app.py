import streamlit as st
import boto3
import datetime
from upload_s3 import get_file
from adschatsum import adssum
from adschatcontent import adscontent
from upload_txt import get_file_txt
from QA import letschat

# Set the title of the app
#st.set_page_config(page_title="Enhanace Search using AWS Bedrock")


# Create a function for each menu option
def option1():
    st.title("Chat with your Document")
    get_file()
    letschat()
def option2():
    st.title("Content Generation")
    get_file_txt()
    

def option3():
    st.title("Summarization")
    adssum()

# Create the menu
menu_options = ["Chat with your Document", "Content Generation", "Summarization"]
selected_option = st.sidebar.selectbox("Choose an option:", menu_options)

# Display the selected option
if selected_option == "Chat with your Document":
    option1()
elif selected_option == "Content Generation":
    option2()
elif selected_option == "Summarization":
    option3()
