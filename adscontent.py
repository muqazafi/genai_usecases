import json
import os
import sys
from dotenv import load_dotenv
import boto3
import botocore.config
from langchain.embeddings import BedrockEmbeddings
from langchain.llms.bedrock import Bedrock
from langchain.load.dump import dumps
from langchain.prompts import PromptTemplate
#from utils import print_ww


module_path = ".."
sys.path.append(os.path.abspath(module_path))



os.environ["AWS_DEFAULT_REGION"] = "us-east-1" 


module_path = ".."
sys.path.append(os.path.abspath(module_path))

load_dotenv()
# configure Bedrock client
boto3.setup_default_session(profile_name=os.getenv("profile_name"))
config = botocore.config.Config(connect_timeout=120, read_timeout=120)
bedrock = boto3.client('bedrock-runtime', 'us-east-1', endpoint_url='https://bedrock-runtime.us-east-1.amazonaws.com',
                       config=config)
                       
llm = Bedrock(
    model_id="anthropic.claude-v2", client=bedrock, model_kwargs={"max_tokens_to_sample": 200}
)
bedrock_embeddings = BedrockEmbeddings(client=bedrock)

inference_modifier = {'max_tokens_to_sample':4096, 
                      "temperature":0.9,
                      "top_k":250,
                      "top_p":1,
                      "stop_sequences": ["\n\nHuman"]
                     }

textgen_llm = Bedrock(model_id = "anthropic.claude-v2",
                    client = bedrock, 
                    model_kwargs = inference_modifier
#                    model_kwargs={"max_tokens_to_sample": 200}
                    )


def main(user_query, template):
    
    user_input=user_query
    mytemplate=template
    # Create a prompt template that has multiple input variables
    multi_var_prompt = PromptTemplate(
#        input_variables=["input", "customerServiceManager", "customerName", "SampleMemorandum"],
        input_variables=["input", "customerServiceManager", "SampleMemorandum"],
        template="""
    Human: {input} from  {customerServiceManager} as same as the following sample: 
    <letter_template>
    {SampleMemorandum}
    </letter_template>
    
    Assistant:"""
    )
    
    # Pass in values to the input variables
    prompt = multi_var_prompt.format(customerServiceManager="Excutive Office of the President", 
#                                     customerName="The House",
                                     input= user_input,
                                     SampleMemorandum=mytemplate
    
         )
         
    num_tokens = textgen_llm.get_num_tokens(prompt)
    print(f"Our prompt has {num_tokens} tokens")
#    user_input = user_query
    response = textgen_llm(prompt)
    result = response[response.index('\n')+1:]
    return(result)
    
    
def main2(prompt):
    num_tokens = textgen_llm.get_num_tokens(prompt)
    print(f"Our prompt has {num_tokens} tokens")
#    user_input = user_query
    response = textgen_llm(prompt)
    
    result = response[response.index('\n')+1:]
    
    return(result)
                        
                    