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

st.set_page_config(layout='wide', page_title='Cymbal Advisor', page_icon = favicon, initial_sidebar_state="expanded" )

st.logo('images/investments.png')

st.header("Welcome")
st.image('images/investments.png')

st.markdown(footer,unsafe_allow_html=True)

