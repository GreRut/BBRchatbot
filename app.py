from dotenv import load_dotenv
import streamlit as st

def main():
    load_dotenv()
    st.set_page_config(page_title="Check PDF")
    st.header("Ask PDF")

    pdf = st.file_uploader("Upload your PDF", type="pdf")

if __name__ == '__main__':
    main()
