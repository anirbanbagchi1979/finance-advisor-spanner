import streamlit as st
import streamlit.components.v1 as components

from jinja2 import Environment, FileSystemLoader

st.set_page_config(layout='wide')

def render_html_template(url, table_template, width=1200, height=600, scrolling=True):
    # Load Jinja environment
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(table_template)

    # Render the template with the provided URL
    rendered_html = template.render(data_source_url=url)

    # Render the HTML content
    st.components.v1.html(rendered_html, width=width, height=height, scrolling=scrolling)


def main():
    template = 'table_template.html'

    st.title('Miles per Gallon Dataset')
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv'
    render_html_template(url, template, width=1300, height=600, scrolling=True)


if __name__ == '__main__':
    main()