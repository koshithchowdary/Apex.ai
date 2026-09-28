import streamlit as st
from core.agent import ApexAgent
from core.config import Settings
from core.retrieval import extract_upload
st.set_page_config(page_title="Apex AI",page_icon="⚡",layout="wide")
st.title("⚡ Apex AI")
st.caption("Reasoning • web research • memory • document context • evaluation")
if "agent" not in st.session_state: st.session_state.agent=None
if "messages" not in st.session_state: st.session_state.messages=[]
with st.sidebar:
    model=st.selectbox("Model",["gpt-5.6-sol","gpt-5.6-terra","gpt-5.6-luna"])
    effort=st.selectbox("Reasoning effort",["high","medium","low"])
    web=st.toggle("Web research",True)
    upload=st.file_uploader("Reference document",type=["pdf","txt","md","csv","json"])
    if st.button("Clear memory"):
        if st.session_state.agent: st.session_state.agent.memory.clear()
        st.session_state.messages=[]; st.rerun()
settings=Settings(model=model,reasoning_effort=effort)
try:
    if st.session_state.agent is None or st.session_state.agent.settings!=settings: st.session_state.agent=ApexAgent(settings)
except ValueError as e: st.error(str(e)); st.stop()
for role,msg in st.session_state.messages:
    with st.chat_message(role): st.markdown(msg)
if prompt:=st.chat_input("Ask Apex anything..."):
    st.session_state.messages.append(("user",prompt))
    with st.chat_message("user"): st.markdown(prompt)
    doc=""
    if upload:
        try: doc=extract_upload(upload.name,upload.getvalue())
        except Exception as e: st.error(f"Document error: {e}")
    with st.chat_message("assistant"):
        with st.spinner("Apex is working..."):
            ans,_=st.session_state.agent.answer(prompt,doc,web)
            st.markdown(ans)
    st.session_state.messages.append(("assistant",ans))
