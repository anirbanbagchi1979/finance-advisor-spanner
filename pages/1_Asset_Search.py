import streamlit as st
import pandas as pd
import numpy as np
from itables.streamlit import interactive_table
import pyarrow
from streamlit.components.v1 import html
from streamlit.components.v1.components import MarshallComponentException
from PIL import Image
from streamlit_navigation_bar import st_navbar
import pages as pg
from database import *
from css import *
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.grid import grid 

st.set_page_config(layout='wide', page_title='Cymbal Advisor', page_icon = favicon, initial_sidebar_state="expanded", )
st.logo('images/investments.png')

def asset_search():
    st.header("Cymbal Fund Advisor")
    st.subheader("Asset Search")

    classes_col, buttons_col, style_col, render_with_col = st.columns(
        [0.25, 0.25, 0.20, 0.10]
    )
    classes = ["display", "compact", "cell-border", "stripe"]
    buttons = ["pageLength",  "csvHtml5", "excelHtml5", "colvis"]
    render_with = "itables"
    style = "table-layout:auto;width:auto;margin:auto;caption-side:bottom"
    it_args = dict(
        classes=classes,
        style=style,
    )

    if buttons:
        it_args["buttons"] = buttons

    # st.subheader('Funds Matching your Search')
    query_params = []
    query_params.append(investment_strategy)
    query_params.append(investment_manager)
    data_load_state = st.text('Loading data...')
    returnVals = fts_query(query_params)
    spanner_query =returnVals.get('query')
    data = returnVals.get('data')

    with st.expander("Spanner Query"):
        with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
        }
        """,
        ):
            st.code(spanner_query,language="sql", line_numbers=False)
    data_load_state.text('Loading data...done!')
    interactive_table(data, caption="Fund Choices for You", **it_args)

with st.sidebar:
    
    with st.form("Asset Search"):
        st.subheader('Search Criteria')
        preciseVsText = st.radio("",["Full-Text", "Precise"],horizontal=True)
        with st.expander("Asset Strategy",expanded=True):
            investment_strategy_pt1 = st.text_input("", value="Europe")
            andOrExclude = st.radio("",["AND", "OR", "EXCLUDE"],horizontal=True)
            investment_strategy_pt2 = st.text_input("", value="Asia")
        investment_manager = st.text_input("Investment Manager", value="")
        if(preciseVsText == 'Full-Text'):
            if(andOrExclude == 'EXCLUDE'):
                investment_strategy = investment_strategy_pt1 + " -" + investment_strategy_pt2
            else:
                investment_strategy = investment_strategy_pt1 + " "+ andOrExclude +" "+ investment_strategy_pt2
        else:
            st.error("Precise Search Not Implemented")
        asset_search_submitted = st.form_submit_button("Submit")
if(asset_search_submitted):
    asset_search()

st.markdown(footer,unsafe_allow_html=True)
