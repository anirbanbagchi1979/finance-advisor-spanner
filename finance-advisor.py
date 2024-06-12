from database import *

import streamlit as st
import pandas as pd
import numpy as np
from itables.streamlit import interactive_table
import pyarrow
import streamlit as st
from itables.streamlit import interactive_table
from streamlit.components.v1 import html
from streamlit.components.v1.components import MarshallComponentException

st.set_page_config(layout='wide')
logo_col, title_col = st.columns([0.1, 0.9])
with logo_col:
    st.markdown(
        "![Cymbal Advisor](https://raw.githubusercontent.com/mwouts/itables/main/src/itables/logo/logo.svg)"
    )
with title_col:
    html(
        """
         <h1>
         <a href="https://mwouts.github.io/itables">Cymbal Fund Advisor</a>
         <h2>Search for your best Investment
         </h2>
        <script src="https://buttons.github.io/buttons.js"></script>"""
    )

st.subheader('Search Criteria')
investment_strategy = st.text_input("Investment Strategy", value="")
investment_manager = st.text_input("Investment Manager", value="")

search_btn = st.button('Search for Best Funds..')

   
classes_col, buttons_col, style_col, render_with_col = st.columns(
    [0.25, 0.25, 0.20, 0.10]
)
classes = ["display", "compact", "cell-border", "stripe"]
# classes = classes_col.multiselect(
#     "Classes",
#     options=["display", "nowrap", "compact", "cell-border", "stripe"],
#     default=["display", "compact"],
# )
buttons = ["pageLength",  "csvHtml5", "excelHtml5", "colvis"]
# buttons = buttons_col.multiselect(
#     "Buttons",
#     options=["pageLength",  "csvHtml5", "excelHtml5", "colvis"],
#     default=["pageLength",  "csvHtml5", "excelHtml5", "colvis"],
# )
render_with = "itables"
# render_with = render_with_col.selectbox(
#     "Render with", ["st.dataframe",  "itables"], index=1
# )

style = "table-layout:auto;width:auto;margin:auto;caption-side:bottom"

# style = style_col.text_input(
#     "Style", value="table-layout:auto;width:auto;margin:auto;caption-side:bottom"
# )

it_args = dict(
    classes=classes,
    style=style,
)
if buttons:
    it_args["buttons"] = buttons

st.subheader('Funds Matching your Search')
query_params = []
query_params.append(investment_strategy)
query_params.append(investment_manager)
if search_btn:
    data_load_state = st.text('Loading data...')
    data = fts_query(query_params)
    data_load_state.text('Loading data...done!')
    interactive_table(data, caption="Fund Choices for You", **it_args)
