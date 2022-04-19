import streamlit as st
import pandas as pd

def About():
    st.write("")
    stock_forecast = st.beta_expander("Stock Market Forecast", expanded=False)
    with stock_forecast:
        st.write("Stock Market Forecasting")
        message = 'The project, created by Slapsoils, is a stock market forecasting software that addresses the dimensionality and expectancy of a new investor. Since stock markets are unpredictable as the fluctuations in the prices over time depend on several factors, the view towards the stock market among the society is that it is highly risky for investment or not suitable for trade which causes people or novice investors to doubt and lose interest to invest. With the use of python package: yfinance and yahooquery, and web scraping, Slapsoils created a python-based software that can analyze, model, and forecast the trends and macro-fluctuations of the stock market based on the gathered Data.'
        st.info(message)

    st.write("")
    developer_ex = st.beta_expander("Developer", expanded=False)
    with developer_ex:
        st.subheader("Team Slapsoil")
        st.write("")
        st.write("")
        dev_email = "contact.email@dlsud.edu.ph"
        img1, img2, img3, img4, img5, img6, img7 = st.beta_columns([0.5, 1, 0.5, 1, 0.5, 1, 0.5])
        with img2:
            st.image('data//developer1.png')
            st.write("")
            st.write("")
            st.write("")
            dev1 = "CO"
            dev11 = 'Paolo Henry'
            st.markdown(
                f"<p style='text-align: center;font-weight: bold; color: #FFFFFF;font-size: 30px;'>{dev1}</p>",
                unsafe_allow_html=True)
            st.markdown(
                f"<p style='text-align: center; color: #FFFFFF;font-size: 20px;'>{dev11}</p>",
                unsafe_allow_html=True)
            dev_email = "(" + dev_email + ")"
            aye = '[c_oloap@forecaststockmarket.tech]' + dev_email
            st.markdown(aye, unsafe_allow_html=True)
        with img4:
            st.image('data//developer1.png')
            st.write("")
            st.write("")
            st.write("")
            dev2 = "FATALLA"
            dev21 = 'Mark'
            st.markdown(
                f"<p style='text-align: center;font-weight: bold; color: #FFFFFF;font-size: 30px;'>{dev2}</p>",
                unsafe_allow_html=True)
            st.markdown(
                f"<p style='text-align: center; color: #FFFFFF;font-size: 20px;'>{dev21}</p>",
                unsafe_allow_html=True)
            dev_email = "(" + dev_email + ")"
            aye = '[mfatalla@forecaststockmarket.tech]' + dev_email
            st.markdown(aye, unsafe_allow_html=True)

        with img6:
            st.image('data//developer1.png')
            st.write("")
            st.write("")
            st.write("")
            dev3 = "GUTIERREZ"
            dev31 = 'Kenn Carlo'
            st.markdown(
                f"<p style='text-align: center;font-weight: bold; color: #FFFFFF;font-size: 30px;'>{dev3}</p>",
                unsafe_allow_html=True)
            st.markdown(
                f"<p style='text-align: center; color: #FFFFFF;font-size: 20px;'>{dev31}</p>",
                unsafe_allow_html=True)
            dev_email = "(" + dev_email + ")"
            aye = '[kenngxx@forecaststockmarket.tech]' + dev_email
            st.markdown(aye, unsafe_allow_html=True)

        with img1:
            st.write("")
        with img3:
            st.write("")
        with img5:
            st.write("")
        with img7:
            st.write("")
    st.write("")
    project_depend = st.beta_expander("Project Dependencies", expanded=False)
    with project_depend:
        first_col = ['streamlit', 'pandas', 'request', 'bs4', 'beautifulsoup4', 'lmxl', 'yfinance', 'plotly', 'numpy', 'matploblib', 'yahooquery','plotly','statsmodel','pmdarima', 'scikit-learn']
        second_col = ['0.84.0', '1.2.4', '2.25.1', '0.0.1', '4.9.3', '4.6.3', '0.1.59', '4.14.3', '1.20.2', '3.4.2', '2.2.15', '4.14.3', '0.12.2', '1.8.2', '0.24.2']
        requirements = pd.DataFrame(
            {"Dependencies": list(first_col), "Version": list(second_col)})
        requirements.index = [""] * len(requirements)
        st.subheader("Requirements")
        st.table(requirements)
    st.write("")
    git_hub = st.beta_expander("Project Host ", expanded=False)
    with git_hub:
        git_hub_link2 = 'https://github.com/mfatalla/StockMarket_Beta'
        git_hub_link2 = '(' + git_hub_link2 + ')'
        git_hub_link_p = '[https://github.com/mfatalla/StockMarket_Beta]' + git_hub_link2
        st.markdown(git_hub_link_p, unsafe_allow_html=True)
        streamlit_link = 'https://share.streamlit.io/mfatalla/stockmarket_beta/main/beta_test.py'
        streamlit_link = '(' + streamlit_link + ')'
        streamlit_link_p = '[https://share.streamlit.io/mfatalla/stockmarket_beta/main/beta_test.py]' + streamlit_link
        st.markdown(streamlit_link_p, unsafe_allow_html=True)
