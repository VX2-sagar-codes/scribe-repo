import streamlit as st
st.title("Scribe :green[Markdown]", text_alignment="center")
st.divider()
option = st.pills(label="Choose your editor", options=["Create a file", "Preview for an uploaded file"])
if option == "Create a file":
 text = st.text_area("Write your markdown here")
 st.header("Preview")
 st.divider()
 if len(text) == 0:
    st.markdown("## _Not available now_")
 elif len(text) > 0:
    with st.container(border=True):
        st.markdown(f"{text}")
    with st.popover("Download File"):
        name = st.text_input("File name")
        if len(name) > 0:
            st.download_button(label="Download", data= text, file_name=(f"{name}.md"), on_click="ignore", type="primary")
elif option == "Preview for an uploaded file":
   uploaded_file = st.file_uploader("Upload a text file", type=["txt", "md"])
   if uploaded_file is not None:
     file_bytes = uploaded_file.read()
     text_content = file_bytes.decode("utf-8")
     st.title("Preview")
     with st.container(border=True):
      st.markdown(text_content)