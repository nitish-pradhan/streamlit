import pandas as pd
import streamlit as st
import altair as alt
import plotly.graph_objects as go
from datetime import datetime

def plot_qualys_line(start_date, end_date):

    df = pd.read_csv('./qualys_status.csv')
    df = df.fillna(0)
    df = df.groupby(['DATE']).sum().reset_index()
    #print(df.head()

    df = df.loc[(df['DATE'] >= start_date) & (df['DATE'] <= end_date)]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['DATE'],
        y=df['FOUND'],
        name='Found',
        line=dict(color='green', width=2)
    ))

    fig.add_trace(go.Scatter(
        x=df['DATE'],
        y=df['NOT_FOUND'],
        name = '<b>Not</b> Found',
        connectgaps=True,
        line=dict(color='red', width=2)
    ))

    fig.update_layout(title='Qualys Status By Date',
                    xaxis_title='Date',
                    yaxis_title='Qualys Status Count')

    return fig


if __name__ == '__main__':

    # col1, col2 = st.columns(2)

    # with col1:
        st.header('Qualys status using Plotly')
        min_date = datetime(2022, 12, 15)
        max_date = datetime(2023, 1, 2)

        a_date = st.date_input("Pick a date range", (min_date, max_date))
        #st.write(a_date[0], a_date[1])
        button_clicked = st.button('Submit', key='qualys_submit')
        if button_clicked:
            fig = plot_qualys_line(str(a_date[0]), str(a_date[1]))
            st.plotly_chart(fig)
    
    # with col2:
    #     st.header('Second Graph will be placed here')