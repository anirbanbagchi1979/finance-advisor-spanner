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

st.set_page_config(
    layout="wide",
    page_title="Cymbal Advisor",
    page_icon=favicon,
    initial_sidebar_state="expanded",
)
st.logo("images/investments.png")


def asset_semantic_search():
    st.header("Cymbal Fund Advisor")
    st.subheader("Semantic Search")

    classes_col, buttons_col, style_col, render_with_col = st.columns(
        [0.25, 0.25, 0.20, 0.10]
    )
    classes = ["display", "compact", "cell-border", "stripe"]
    buttons = ["pageLength", "csvHtml5", "excelHtml5", "colvis"]
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
    data_load_state = st.text("Loading data...")
    returnVals = semantic_query(query_params)
    spanner_query = returnVals.get("query")
    data = returnVals.get("data")

    with st.expander("Spanner Query"):
        with stylable_container(
            "codeblock",
            """
        code {
            white-space: pre-wrap !important;
        }
        """,
        ):
            st.code(spanner_query, language="sql", line_numbers=False)
    data_load_state.text("Loading data...done!")
    interactive_table(data, caption="Fund Choices for You", **it_args)


with st.sidebar:

    with st.form("Asset Semantic Search"):
        st.subheader("Search Criteria")
        investment_strategy = st.text_area(
            "Search for me",
            value="Invest in companies which also subscribe to my ideas around climate change, doing good for the planet",
        )
        investment_manager = st.text_input("Investment Manager", value="")
        asset_semantic_search_submitted = st.form_submit_button("Submit")
if asset_semantic_search_submitted:
    asset_semantic_search()

st.markdown(footer, unsafe_allow_html=True)
