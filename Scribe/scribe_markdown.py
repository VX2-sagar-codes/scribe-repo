import streamlit as st
st.set_page_config(
   page_title="Scribe markdown",
   page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2pBTgqfFd-Z_H-m-8ipGgOhqawx0W_0bMDVN6Xur1fjMefxCXKd3gMkg&s=10"
)
st.title("Scribe :green[Markdown]", text_alignment="center")
st.divider()
with st.sidebar:
   st.title(":rainbow[Explore]")
   cheatsheet = st.checkbox(label="Get a cheatsheet")
   if cheatsheet:
      st.markdown("""# Cheatsheet
| Name | Code |
| --- | --- |
| Header | ``` # (write)``` | 
| **Bold** | ``` ** (write) ** ``` |
| _Italic_ | ``` _(write)_ ```|
| $LaTeX$ | ``` $(write)$ ``` |
| >Blockquote | ``` >(write)``` |
| ~strike~ | ```~(write)~```|
| [link](https://example.com) | ```[name](link)``` |
| image | ```[Alt text](path/to/image)```|
| codespace | ``` ```(write)``` ``` |
""")
option = st.pills(label="Choose your editor", options=["Create a file", "Preview for an uploaded file"])
if option == "Create a file":
    text = st.text_area("Write your markdown here")
    st.divider()
    if len(text) == 0:
      st.markdown("## _Not available now_")
    elif len(text) > 0:
      choice = st.segmented_control(label="Choose", options=["Preview", "Stats"])
      if choice == "Preview":
       st.header("Preview", text_alignment="center")
       with st.container(border=True):
          st.markdown(f"{text}")
      elif choice == "Stats":
       col1, col2, col3 = st.columns(3)
       with col1:
          st.metric(label="Chars", value=len(text))
       with col2:
          st.metric(label="Words", value=len(text.split()))
       with col3:
          st.metric(label="Lines", value=len(text.splitlines()))
       st.divider()
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