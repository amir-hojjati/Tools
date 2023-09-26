import os
import sys

import streamlit as st
from streamlit import runtime
from streamlit.web import cli as stcli
import pandas as pd

from search import search_csv


def main():
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data)

        keyword = st.text_input('Enter a keyword or regex pattern to search')

        if st.button('Search'):
            results = search_csv(keyword, data)
            if results.empty:
                st.write('No results found')
            else:
                st.write(results)
                st.download_button(
                   "Download CSV",
                   results.to_csv(index=False).encode('utf-8'),
                   "file.csv",
                   "text/csv",
                   key='download-csv'
                )


if __name__ == '__main__':
    if runtime.exists():
        main()
    else:
        script = os.path.realpath(__file__)
        sys.argv = ["streamlit", "run", script, '--server.headless', 'true']
        sys.exit(stcli.main())
