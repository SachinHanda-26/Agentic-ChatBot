import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}
        
    def load_streamlit_ui(self):
        st.set_page_config(page_title="ChatBot " + self.config.get_page_title(), layout="wide")
        st.header("ChatBot " + self. config. get_page_title())
        
        with st.sidebar:
# Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

# LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

# Model selection
            if self.user_controls["selected_llm"] == 'Groq':
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Groq Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]=st.text_input("API Key", type="password")
                if not self.user_controls["GROQ_API_KEY"]:
                  st.warning(" A Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com")


## UseCase selection
            self.user_controls["selected_usecase"]=st. selectbox("Select UseCases", usecase_options)
            
            if self.user_controls["selected_usecase"] == "Chatbot With Tool":
               os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("Tavily API Key", type="password")
                
               if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your Tavily API key to proceed. Don't have? refer : https://tavily.com/")
        
        
        return self.user_controls

            