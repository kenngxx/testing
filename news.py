import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd

def News(asset):

    if "page" not in st.session_state:
        st.session_state.page = 0
        st.session_state.count = 5

    def next_page():
        st.session_state.page += 1
        st.session_state.count += 5

    def prev_page():
        st.session_state.page -= 1
        st.session_state.count -= 5

    if "page2" not in st.session_state:
        st.session_state.page2 = 0
        st.session_state.count2 = 5
    if "count2" not in st.session_state:
        st.session_state.page2 = 0
        st.session_state.count2 = 5

    def next_page2():
        st.session_state.page2 += 1
        st.session_state.count2 += 5

    def prev_page2():
        st.session_state.page2 -= 1
        st.session_state.count2 -= 5

    trend_today = st.beta_expander("Trend Today", expanded=True)
    with trend_today:
        col1, col2, col3 = st.beta_columns([1,3,1])
        with col1:
            st.write("")
        with col2:
            trend_url = 'https://stockanalysis.com/news/all-stocks/'
            trend_page = requests.get(trend_url)
            trend_soup = BeautifulSoup(trend_page.text, 'lxml')

            trend_table = trend_soup.find('table', {'class': 'sidetable'})
            trend_header = []

            for c_r in trend_table.find_all('th'):
                header = c_r.text.strip()
                trend_header.append(header)

            trend_df = pd.DataFrame(columns=trend_header)

            for trend_row in trend_table.find_all('tr')[1:]:
                trend_data = trend_row.find_all('td')
                trend_row_data = [trend_td.text.strip() for trend_td in trend_data]
                trend_length = len(trend_df)
                trend_df.loc[trend_length] = trend_row_data

            trend_df.set_index('Symbol', inplace=False)

            sub_head1 = 'Trending Ticker'
            st.markdown(
                f"<p style='vertical-align:bottom;font-weight: bold; color: #FFA500;font-size: 20px;'>{sub_head1}</p>",
                unsafe_allow_html=True)
            st.table(trend_df)
        with col3:
            st.write("")

    Cnews = st.beta_expander("Company News", expanded=True)
    with Cnews:
        endp = st.session_state.count
        startp = endp - 5
        url = 'https://stockanalysis.com/stocks/' + asset
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        x = 0
        for x in range(startp, endp):
            newsTitle = soup.find_all('div', {'class': 'news-side'})[x].find('div').text
            newsThumbnail = soup.find_all('div', {'class': 'news-img'})[x].find('img')
            newsBody = soup.find_all('div', {'class': 'news-text'})[x].find('p').text
            subMeta = soup.find_all('div', {'class': 'news-meta'})[x].find_next('span').text
            hreflink = soup.find_all('div', {'class': 'news-img'})[x].find('a')
            link = hreflink.get('href')
            wap = newsThumbnail.get('data-src')
            chart1, chart2, chart3 = st.beta_columns([1, 2, 1])
            with chart1:
                st.image(wap)
            with chart2:
                st.markdown(f"<h1 style='font-weight: bold; font-size: 17px;'>{newsTitle}</h1>",
                            unsafe_allow_html=True)
                st.markdown(newsBody)
                link = "(" + link + ")"
                aye = '[[Link]]' + link
                st.markdown("Source: " + aye, unsafe_allow_html=True)
                st.text(" ")
                st.text(" ")
            with chart3:
                st.markdown(subMeta)
        st.text(" ")
        st.write("")
        col1, col2, col3, _ = st.beta_columns([0.1, 0.17, 0.1, 0.63])
        if st.session_state.page < 4:
            col3.button(">", on_click=next_page)
        else:
            col3.write("")  # t
            # his makes the empty column show up on mobile
        if st.session_state.page > 0:
            col1.button("<", on_click=prev_page)
        else:
            col1.write("")  # this makes the empty column show up on mobile
        col2.write(f"Page {1 + st.session_state.page} of {5}")
    Onews = st.beta_expander("Stock Market News", expanded=False)
    with Onews:
        Oendp = st.session_state.count2
        Ostartp = Oendp - 5
        url = 'https://stockanalysis.com/news'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1', {'class': 'entry-title'}).text
        x = 0
        for x in range(Ostartp, Oendp):
            newsTitle1 = soup.find_all('div', {'class': 'news-side'})[x].find('div').text
            time1 = soup.find_all('div', {'class': 'news-meta'})[x].find('span').text
            newsThumbnail1 = soup.find_all('div', {'class': 'news-img'})[x].find('img')
            newsBody1 = soup.find_all('div', {'class': 'news-text'})[x].find('p').text
            hreflink1 = soup.find_all('div', {'class': 'news-img'})[x].find('a')
            link1 = hreflink1.get('href')
            newsimg1 = newsThumbnail1.get('data-src')
            chart1, chart2, chart3 = st.beta_columns([1, 2, 1])
            with chart1:
                st.image(newsimg1)
            with chart2:
                st.markdown(f"<h1 style='font-weight: bold; font-size: 17px;'>{newsTitle1}</h1>",
                            unsafe_allow_html=True)
                st.markdown(newsBody1)
                link1 = "(" + link1 + ")"
                concatclink = '[[Link]]' + link1
                st.markdown("Source: " + concatclink, unsafe_allow_html=True)
                st.text(" ")
                st.text(" ")
            with chart3:
                st.markdown(time1)
        st.text(" ")
        st.text(" ")
        col1, col2, col3, _ = st.beta_columns([0.1, 0.17, 0.1, 0.63])
        if st.session_state.page2 < 4:
            col3.button("> ", on_click=next_page2)
        else:
            col3.write("")  # t
            # his makes the empty column show up on mobile
        if st.session_state.page > 0:
            col1.button("< ", on_click=prev_page2)
        else:
            col1.write("")  # this makes the empty column show up on mobile
        col2.write(f"Page {1 + st.session_state.page2} of {5}")