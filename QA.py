import boto3
import streamlit as st
from langchain_community.retrievers import AmazonKnowledgeBasesRetriever
import json
from send_email import send_email

#st.subheader('RAG Using Knowledge Base from Amazon Bedrock', divider='rainbow')
endpoint_url="https://bedrock-runtime.us-east-1.amazonaws.com"
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message['text'])


bedrockClient = boto3.client('bedrock-agent-runtime', 'us-east-1')
knowledge_base_id='1CUEAPUPQW'


def getAnswers(questions):
#    client=self._return_aws_service_client(run_time=True)
    knowledgeBaseResponse = bedrockClient.retrieve_and_generate(
        input={'text': questions},
        retrieveAndGenerateConfiguration={
            'knowledgeBaseConfiguration': {
                'knowledgeBaseId': '1CUEAPUPQW',
                'modelArn': 'arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-v2',
                'retrievalConfiguration': {
                        'vectorSearchConfiguration': {
                            'numberOfResults': 100,
                            'overrideSearchType': 'HYBRID'
                        }
                    }
            },
            'type': 'KNOWLEDGE_BASE'
        })
    return knowledgeBaseResponse





def getreply(query):
    response = bedrockClient.retrieve(
    knowledgeBaseId="knowledge-base-rag",
    retrievalQuery={'query':query},
    retrievalConfiguration={
                'vectorSearchConfiguration': {
                    'numberOfResults': 2
                }
            },
            nextToken='loan'
    )
    return response
def open_sidebar():
    st.session_state.sidebar = True

def letschat():
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    for message in st.session_state.chat_history:
        with st.chat_message(message['role']):
            st.markdown(message['text'])

    message_placeholder = st.empty()
    questions = st.chat_input('Enter you questions here...')
    if questions:
        with st.chat_message('user'):
            st.markdown(questions)
          
        st.session_state.chat_history.append({"role":'user', "text":questions})
        with st.spinner("Thinking..."):
         query=json.dumps(questions)
         response = getAnswers(questions)
    
#        st.write(response)
      
        answer = response['output']['text']
    
        with st.chat_message('assistant'):
            with st.spinner("Thinking..."):
                st.markdown(answer)
#            st.write(answer)
        st.session_state.chat_history.append({"role":'assistant', "text": answer})
        
        with st.expander("Not finding what you're looking for?"):
            st.write(
                "Automatically generate a draft for an internal ticket to our support team."
            )
            st.button(
                "Generate ticket",
                type="primary",
                key="show_ticket",
                on_click=send_email(),
            )
        with st.container():
            st.write("&nbsp;")
    
        if len(response['citations'][0]['retrievedReferences']) != 0:
            context = response['citations'][0]['retrievedReferences'][0]['content']['text']
            doc_url = response['citations'][0]['retrievedReferences'][0]['location']['s3Location']['uri']
            
            #Below lines are used to show the context and the document source for the latest Question Answer
            st.markdown(f"<span style='color:#FFDA33'>Context used: </span>{context}", unsafe_allow_html=True)
            st.markdown(f"<span style='color:#FFDA33'>Source Document: </span>{doc_url}", unsafe_allow_html=True)
        
        else:
    #        break
           st.markdown(f"<span style='color:red'>No Context</span>", unsafe_allow_html=True)
 
if __name__=="__main__":
    letschat()
    