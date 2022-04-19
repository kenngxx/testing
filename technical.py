import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime as dt

def Scrappy(tickerinput):
    def calcMovingAverage(datatech, size):
        dftech = datatech.copy()
        dftech['sma'] = dftech['Adj Close'].rolling(size).mean()
        dftech['ema'] = dftech['Adj Close'].ewm(span=size, min_periods=size).mean()
        dftech.dropna(inplace=True)
        return dftech
    def calc_macd(datatech):
        dftech = datatech.copy()
        dftech['ema12'] = dftech['Adj Close'].ewm(span=12, min_periods=12).mean()
        dftech['ema26'] = dftech['Adj Close'].ewm(span=26, min_periods=26).mean()
        dftech['macd'] = dftech['ema12'] - dftech['ema26']
        dftech['signal'] = dftech['macd'].ewm(span=9, min_periods=9).mean()
        dftech.dropna(inplace=True)
        return dftech
    def calcBollinger(datatech, size):
        dftech = datatech.copy()
        dftech["sma"] = dftech['Adj Close'].rolling(size).mean()
        dftech["bolu"] = dftech["sma"] + 2 * dftech['Adj Close'].rolling(size).std(ddof=0)
        dftech["bold"] = dftech["sma"] - 2 * dftech['Adj Close'].rolling(size).std(ddof=0)
        dftech["width"] = dftech["bolu"] - dftech["bold"]
        dftech.dropna(inplace=True)
        return dftech
    st.title('Technical Indicators')
    st.subheader('Moving Average')
    coMA1, coMA2 = st.beta_columns(2)
    with coMA1:
        numYearMA_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 10]
        query_params = st.experimental_get_query_params()
        default = int(query_params["numYearMA"][0]) if "numYearMA" in query_params else 1
        numYearMA = st.selectbox(
            "Insert period (Year): ",
            numYearMA_list1,
            index=default
        )
    with coMA2:
        windowSizeMA_list2 = [1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15,16,17,18,19,20]
        query_params3 = st.experimental_get_query_params()
        default = int(query_params3["windowSizeMA"][0]) if "windowSizeMA" in query_params3 else 19
        windowSizeMA = st.selectbox(
            "Window Size (Day): ",
            windowSizeMA_list2,
            index=default
        )
    start_tech = dt.datetime.today() - dt.timedelta(numYearMA * 365)
    end_tech = dt.datetime.today()
    dataMA = yf.download(tickerinput, start_tech, end_tech)
    df_ma = calcMovingAverage(dataMA, windowSizeMA)
    df_ma = df_ma.reset_index()
    figMA = go.Figure()
    figMA.add_trace(
        go.Scatter(
            x=df_ma['Date'],
            y=df_ma['Adj Close'],
            name="Prices Over Last " + str(numYearMA) + " Year(s)"
        )
    )
    figMA.add_trace(
        go.Scatter(
            x=df_ma['Date'],
            y=df_ma['sma'],
            name="SMA" + str(windowSizeMA) + " Over Last " + str(numYearMA) + " Year(s)"
        )
    )
    figMA.add_trace(
        go.Scatter(
            x=df_ma['Date'],
            y=df_ma['ema'],
            name="EMA" + str(windowSizeMA) + " Over Last " + str(numYearMA) + " Year(s)"
        )
    )
    figMA.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))
    figMA.update_layout(legend_title_text='Trend')
    figMA.update_yaxes(tickprefix="$")
    st.plotly_chart(figMA, use_container_width=True)
    st.subheader('Moving Average Convergence Divergence (MACD)')
    numYearMACD_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 10]
    query_params2 = st.experimental_get_query_params()
    default = int(query_params2["numYearMACD"][0]) if "numYearMACD" in query_params2 else 1
    numYearMACD = st.selectbox(
        " Insert period (Year):  ",
        numYearMACD_list1,
        index=default
    )
    startMACD = dt.datetime.today() - dt.timedelta(numYearMACD * 365)
    endMACD = dt.datetime.today()
    dataMACD = yf.download(tickerinput, startMACD, endMACD)
    df_macd = calc_macd(dataMACD)
    df_macd = df_macd.reset_index()
    figMACD = make_subplots(rows=2, cols=1,
                            shared_xaxes=True,
                            vertical_spacing=0.01)
    figMACD.add_trace(
        go.Scatter(
            x=df_macd['Date'],
            y=df_macd['Adj Close'],
            name="Prices Over Last " + str(numYearMACD) + " Year(s)"
        ),
        row=1, col=1
    )
    figMACD.add_trace(
        go.Scatter(
            x=df_macd['Date'],
            y=df_macd['ema12'],
            name="EMA 12 Over Last " + str(numYearMACD) + " Year(s)"
        ),
        row=1, col=1
    )
    figMACD.add_trace(
        go.Scatter(
            x=df_macd['Date'],
            y=df_macd['ema26'],
            name="EMA 26 Over Last " + str(numYearMACD) + " Year(s)"
        ),
        row=1, col=1
    )
    figMACD.add_trace(
        go.Scatter(
            x=df_macd['Date'],
            y=df_macd['macd'],
            name="MACD Line"
        ),
        row=2, col=1
    )
    figMACD.add_trace(
        go.Scatter(
            x=df_macd['Date'],
            y=df_macd['signal'],
            name="Signal Line"
        ),
        row=2, col=1
    )
    figMACD.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="left",
        x=0
    ))
    figMACD.update_yaxes(tickprefix="$")
    st.plotly_chart(figMACD, use_container_width=True)
    st.subheader('Bollinger Band')
    coBoll1, coBoll2 = st.beta_columns(2)
    with coBoll1:
        numYearBoll_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 10]
        query_params4 = st.experimental_get_query_params()
        default = int(query_params4["numYearBoll"][0]) if "numYearBoll" in query_params4 else 1
        numYearBoll = st.selectbox(
            "Insert period (Year) ",
            numYearBoll_list1,
            index=default
        )
    with coBoll2:
        windowSizeBoll_list2 = [1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15,16,17,18,19,20]
        query_params4 = st.experimental_get_query_params()
        default = int(query_params4["windowSizeBoll"][0]) if "windowSizeBoll" in query_params4 else 19
        windowSizeBoll= st.selectbox(
            "Window Size (Day) ",
            windowSizeBoll_list2,
            index=default
        )
    startBoll = dt.datetime.today() - dt.timedelta(numYearBoll * 365)
    endBoll = dt.datetime.today()
    dataBoll = yf.download(tickerinput, startBoll, endBoll)
    df_boll = calcBollinger(dataBoll, windowSizeBoll)
    df_boll = df_boll.reset_index()
    figBoll = go.Figure()
    figBoll.add_trace(
        go.Scatter(
            x=df_boll['Date'],
            y=df_boll['bolu'],
            name="Upper Band"
        )
    )
    figBoll.add_trace(
        go.Scatter(
            x=df_boll['Date'],
            y=df_boll['sma'],
            name="SMA" + str(windowSizeBoll) + " Over Last " + str(numYearBoll) + " Year(s)"
        )
    )
    figBoll.add_trace(
        go.Scatter(
            x=df_boll['Date'],
            y=df_boll['bold'],
            name="Lower Band"
        )
    )
    figBoll.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="left",
        x=0
    ))
    figBoll.update_yaxes(tickprefix="$")
    st.plotly_chart(figBoll, use_container_width=True)
