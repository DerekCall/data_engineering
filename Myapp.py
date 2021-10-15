import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


from sqlalchemy import create_engine
from sqlalchemy import inspect
import sqlite3

st.write("""
# NBA Statistics App
Data Engineering Module at Metis
""")

engine = create_engine("sqlite:///nba_data.db")

st.title("NBA Player Comparison Dashboard")

st.markdown( "This dashboard will allow for player statistics to be compared across multiple categories" )

st.sidebar.title('Select Desired Statistics and Time Frame')

stat_types = selected_status = st.sidebar.selectbox('Select Statistical Categories', options=['Traditional', 'Shooting'])

time_types = selected_status = st.sidebar.selectbox('Select Window of Time', options=['Beginning of Career'])

player_choice1 = st.text_input('First Player')    
player_choice2 = st.text_input('Second Player')

query1 = f'''SELECT  SEASON_ID, AVG(PTS) as AVG_PTS, AVG(STL) as AVG_STL, AVG(REB) as AVG_REB, AVG(AST) as AVG_AST, AVG(FG_PCT) as AVG_FG_PCT, AVG(FGM) as AVG_FGM, AVG(FG3_PCT) as AVG_FG3_PCT, AVG(FTM) as AVG_FTM, AVG(FT_PCT) as AVG_FT_PCT, AVG(FG3M) as AVG_FG3M, AVG(BLK) as AVG_BLK, AVG(TOV) as AVG_TOV, full_name FROM nba_all_games WHERE full_name = '{player_choice1}' GROUP BY SEASON_ID '''

query2 = f'''SELECT  SEASON_ID, AVG(PTS) as AVG_PTS, AVG(STL) as AVG_STL, AVG(REB) as AVG_REB, AVG(AST) as AVG_AST, AVG(FG_PCT) as AVG_FG_PCT, AVG(FGM) as AVG_FGM, AVG(FG3_PCT) as AVG_FG3_PCT, AVG(FTM) as AVG_FTM, AVG(FT_PCT) as AVG_FT_PCT, AVG(FG3M) as AVG_FG3M, AVG(BLK) as AVG_BLK, AVG(TOV) as AVG_TOV, full_name FROM nba_all_games WHERE full_name = "{player_choice2}"  GROUP BY SEASON_ID '''

player1_all_stats_avg = pd.read_sql(query1, engine)
player2_all_stats_avg = pd.read_sql(query2, engine)

if player1_all_stats_avg['full_name'].count() > player2_all_stats_avg['full_name'].count():
    x_tick_length = player1_all_stats_avg['full_name'].count()
else:
    x_tick_length = player2_all_stats_avg['full_name'].count()


#Regular statistics

if stat_types == 'Traditional' and time_types == 'Beginning of Career':

    fig = plt.figure(figsize=[20,21])

    plt.suptitle('Career Averages',fontsize = 34)

    plt.subplot(3,2,1)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_PTS'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_PTS'], linewidth=4)
    plt.title('Points per Game', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)
    plt.legend([player_choice1, player_choice2], fontsize=20)
    

    plt.subplot(3,2,2)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_AST'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_AST'], linewidth=4)
    plt.title('Assists per Game', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)

    plt.subplot(3,2,3)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_REB'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_REB'], linewidth=4)
    plt.title('Rebounds per Game', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)

    plt.subplot(3,2,4)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_STL'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_STL'], linewidth=4)
    plt.title('Steals per Game', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)

    plt.subplot(3,2,5)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_BLK'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_BLK'], linewidth=4)
    plt.title('Blocks per Game', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)
    
    

    plt.subplot(3,2,6)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_TOV'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_TOV'], linewidth=4)
    plt.title('Turnovers per Game', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)

    plt.show()
    st.pyplot(fig)

#Shooting Statistics

if stat_types == 'Shooting' and time_types == 'Beginning of Career':

    fig = plt.figure(figsize=[20,21])

    plt.suptitle('Shooting Statistics',fontsize = 34)

    plt.subplot(3,2,1)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_FGM'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_FGM'], linewidth=4)
    plt.title('Average Field Goals Made', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)
    plt.legend([player_choice1, player_choice2], fontsize=20)
    # plt.xticks(np.linspace(1, x_tick_length, x_tick_length)

    plt.subplot(3,2,2)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_FG_PCT'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_FG_PCT'], linewidth=4)
    plt.title('Average Field Goal Percentage', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)

    plt.subplot(3,2,3)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_FTM'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_FTM'], linewidth=4)
    plt.title('Average Free Throws Made', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)

    plt.subplot(3,2,4)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_FT_PCT'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_FT_PCT'], linewidth=4)
    plt.title('Average Free Throw Percentage', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)

    plt.subplot(3,2,5)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_FG3M'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_FG3M'], linewidth=4)
    plt.title('Made Threes per Game', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)

    plt.subplot(3,2,6)
    plt.plot(player1_all_stats_avg.index, player1_all_stats_avg['AVG_FG3_PCT'], linewidth=4)
    plt.plot(player2_all_stats_avg.index, player2_all_stats_avg['AVG_FG3_PCT'], linewidth=4)
    plt.title('Average Three Point Percentage', size=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)

    plt.show()
    st.pyplot(fig)


