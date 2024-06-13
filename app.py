import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers


# functions to get response from llama 2 model

def getLLamaresponse(input_text,no_words,blog_style):
    
    # LLama2 Model
    llm=CTransformers(model='C:/Users/91997/Desktop/projects/models',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})

    #prompt template
    template="""
        write a blog for{blog_style} job profile for a topic {input_text}
        within{no_words} words.
            """

    prompt= PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                            template= template)

    #generate the response from the LLama 2 model

    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title="Generate Blogs",
                   page_icon="🧊",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Generate Blogs 🧊")

input_text =st.text_input("Enter the Blog Topic")



# creating to more columns for additional 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input("No.of Words")
with col2:
    blog_style=st.selectbox('Writing the blog for', 
                            ('Researches', 'Data Scientist','Common People'),index=0)
        
submit=st.button("Generate")   

#final response

if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style)) 