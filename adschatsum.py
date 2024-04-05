import streamlit as st
from streamlit_chat import message
from streamlit.components.v1 import html
import pandas as pd
from io import StringIO
from adssum import Chunk_and_Summarize

#st.set_page_config(page_title="💬 USAID Chat")

message_placeholder = st.empty()

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

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": ""}]

# Display chat messages


# Function for generating LLM response
#def generate_response(prompt_input):
#    return question(prompt_input)
    
    
def adssum():
# User-provided prompt
    uploaded_file = st.file_uploader('Choose your .pdf file to summarize', type="pdf")
    if uploaded_file is not None:
        with st.spinner("Thinking..."):
         st.write(Chunk_and_Summarize(uploaded_file))
#    uploaded_file = st.file_uploader("Choose a file")
#    if st.session_state.messages[-1]["role"] != "assistant":
#        with st.chat_message("assistant"):
#            with st.spinner("Thinking..."):
#              st.write(Chunk_and_Summarize(uploaded_file))
#             if uploaded_file is not None:
    # To read file as bytes:
#        bytes_data = uploaded_file.getvalue()
       
#        st.write(bytes_data)
#              st.write(Chunk_and_Summarize(uploaded_file))
#              print(Chunk_and_Summarize(uploaded_file))
    # Generate a new response if last message is not from assistant
#    if st.session_state.messages[-1]["role"] != "assistant":
#        with st.chat_message("assistant"):
#            with st.spinner("Thinking..."):
#                response = generate_response(prompt)
    #            message_placeholder.markdown(response)
#                response1=str(response)
    #            response2=[word.replace("\n", "  \n") for word in response1]
    #            new_list = [element.replace('l', '_') for element in my_list]
    #            st.write(newline(response1))
#                st.markdown(newline(response1))
    #            print(response2)
#        message = {"role": "assistant", "content": response}
#        st.session_state.messages.append(message)
