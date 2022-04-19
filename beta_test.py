import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
import yfinance as yf
import profile2
import about
import technical
import news
import overview
import stock_prediction


st.set_page_config(
    page_title='Stock Market Forecasting',
    page_icon='💲',
    layout='wide',
    initial_sidebar_state="expanded",
)

@st.cache(suppress_st_warning=True)
def load_data():
    components = pd.read_html(
        "https://en.wikipedia.org/wiki/List_of_S" "%26P_500_companies"
    )[0]
    return components.drop("SEC filings", axis=1).set_index("Symbol")


@st.cache(suppress_st_warning=True)
def load_quotes(asset):
    return yf.download(asset)


@st.cache(suppress_st_warning=True)
def label(symbol):
    a = components.loc[symbol]
    return symbol + " - " + a.Security

components = load_data()

menu = ['Overview', 'News', 'Technical Indicators','Stock Prediction','Company Profile', 'About']
query_params = st.experimental_get_query_params()
default = int(query_params["menubar"][0]) if "menubar" in query_params else 0
menubar = st.selectbox(
    "Menu",
    menu,
    index=default
)
if menubar:
    st.experimental_set_query_params(menubar=menu.index(menubar))


sidebar_components = st.sidebar.beta_container()

with sidebar_components:

    st.image('data//logo1.png')
    st.subheader("Select asset")
    asset = st.sidebar.selectbox(
        "Click below to select a new asset",
        components.index.sort_values(),
        index=3,
        format_func=label,
    )

    ticker = yf.Ticker(asset)
    info = ticker.info
    url = 'https://stockanalysis.com/stocks/' + asset
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    name = soup.find('h1', {'class': 'sa-h1'}).text
    price = soup.find('span', {'id': 'cpr'}).text
    currency = soup.find('span', {'id': 'cpr'}).find_next('span').text
    change = soup.find('span', {'id': 'spd'}).text
    rate = soup.find('span', {'id': 'spd'}).find_next('span').text
    meta = soup.find('div', {'id': 'sti'}).find('span').text
    try:
        after = soup.find('div', {'id': 'ext'}).find_next('span').text
        after2 = soup.find('span', {'id': 'extc'}).text
        aftert = soup.find('span', {'id': 'extcp'}).text
        aftertime = soup.find('span', {'id': 'exttime'}).text
        CR = change + " (" + rate + ")"
        CT = after2 + " (" + aftert + ")"
        sub = change
        sub2 = after2
        aye = ": After-hours"
    except AttributeError as attriErr:
        after = "NO DATA"
        after2 = "NO DATA"
        aftert = "NO DATA"
        aftertime = "NO DATA"
        CR = "NO DATA"
        CT = "NO DATA"
        sub = "NO DATA"
        sub2 = "NO DATA"
        aye = "NO DATA"

    formtab = st.sidebar.beta_container()
    with formtab:
        st.image(info['logo_url'])
        qq = (info['shortName'])
        st.markdown(
            f"<p style='vertical-align:bottom;font-weight: bold; color: #FFFFFF;font-size: 40px;'>{qq}</p>",
            unsafe_allow_html=True)
        xx = price + " " + currency
        st.markdown(
            f"<p style='vertical-align:bottom;font-weight: bold; color: #FFFFFF;font-size: 20px;'>{xx}</p>",
            unsafe_allow_html=True)
        if sub != "NO DATA" and sub2 != "NO DATA":
            if float(sub) > 0:
                aye2 = "+"
                st.markdown(
                    f"<p style='vertical-align:bottom;font-weight: bold; color: #00AC4A;font-size: 13px;'>{aye2 + CR}</p>",
                    unsafe_allow_html=True)
            else:
                st.markdown(
                    f"<p style='vertical-align:bottom;font-weight: bold; color: #D10000;font-size: 13px;'>{CR}</p>",
                    unsafe_allow_html=True)
            st.markdown(
                f"<p style='vertical-align:bottom;font-weight: italic; color: #FFFFFF;font-size: 10px;'>{meta}</p>",
                unsafe_allow_html=True)
            if float(sub2) > 0:
                st.markdown(after + " " + currency)
                st.markdown(
                    f"<p style='vertical-align:bottom;font-weight: bold; color: #00AC4A;font-size: 13px;'>{CT + aye}</p>",
                    unsafe_allow_html=True)
            else:
                st.markdown(after + " " + currency)
                st.markdown(
                    f"<p style='vertical-align:bottom;font-weight: bold; color: #D10000;;font-size: 13px;'>{CT + aye}</p>",
                    unsafe_allow_html=True)
            st.markdown(
                f"<p style='vertical-align:bottom;font-weight: italic; color: #FFFFFF;font-size: 10px;'>{aftertime}</p>",
                unsafe_allow_html=True)
        else:
            nodata = "NO PRE-MARKET DATA AVAILABLE"
            st.markdown(
                f"<p style='vertical-align:bottom;font-weight: bold; color: #FFFFFF;font-size: 20px;'>{nodata}</p>",
                unsafe_allow_html=True)

if menubar == 'Overview':

    overview.Overview(asset)
elif menubar == 'News':
    news.News(asset)
elif menubar == 'Technical Indicators':
    technical.Scrappy(asset)

elif menubar == 'Stock Prediction':
    stock_prediction.stock_predict(asset)
elif menubar == 'Company Profile':
    profile2.Profile(asset)

elif menubar == 'About':
    about.About()

else:
    st.error("Something has gone terribly wrong.")