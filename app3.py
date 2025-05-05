import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Set page title and custom CSS for design
st.set_page_config(page_title="NBA Stats Dashboard", page_icon="🏀", layout="wide")
st.markdown("""
    <style>
        .main {
            background-color: #f0f0f5;
            color: #333;
            font-family: 'Arial', sans-serif;
        }
        h1, h2, h3 {
            color: #1c3b65;
        }
        .stSidebar {
            background-color: #3b3b3b;
            color: white;
        }
        .stSelectbox {
            color: #1c3b65;
        }
        .stButton {
            background-color: #1c3b65;
            color: white;
        }
        .stPlotlyChart, .stMatplotlib {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.title("NBA Basketball Stats Dashboard")

# Sidebar for User Input
st.sidebar.header("Filters")
players = ['LeBron James', 'Stephen Curry', 'Kevin Durant', 'Giannis Antetokounmpo', 'Luka Dončić']
selected_player = st.sidebar.selectbox("Select Player", players)

# Example API for NBA Player Stats (Replace with actual API)
# Here we use a mock dataset since we can't make API requests in this environment.
player_data = {
    "LeBron James": {
        "Points": 25.0, "Assists": 7.8, "Rebounds": 7.5, "Blocks": 1.1, "Steals": 1.3
    },
    "Stephen Curry": {
        "Points": 29.4, "Assists": 6.3, "Rebounds": 5.2, "Blocks": 0.4, "Steals": 1.3
    },
    "Kevin Durant": {
        "Points": 27.0, "Assists": 5.0, "Rebounds": 6.8, "Blocks": 1.1, "Steals": 0.7
    },
    "Giannis Antetokounmpo": {
        "Points": 28.1, "Assists": 5.9, "Rebounds": 11.0, "Blocks": 1.3, "Steals": 1.0
    },
    "Luka Dončić": {
        "Points": 27.5, "Assists": 8.6, "Rebounds": 8.0, "Blocks": 0.5, "Steals": 1.0
    }
}

# Fetch selected player's data
data = player_data[selected_player]

# Display basic player stats
st.subheader(f"Stats for {selected_player}")
st.write(f"Points per Game: {data['Points']}")
st.write(f"Assists per Game: {data['Assists']}")
st.write(f"Rebounds per Game: {data['Rebounds']}")
st.write(f"Blocks per Game: {data['Blocks']}")
st.write(f"Steals per Game: {data['Steals']}")

# Display player data as a DataFrame for charting
player_stats = {
    "Category": ["Points", "Assists", "Rebounds", "Blocks", "Steals"],
    "Stats": [data["Points"], data["Assists"], data["Rebounds"], data["Blocks"], data["Steals"]]
}
df = pd.DataFrame(player_stats)

# Layout with columns for displaying charts side by side
col1, col2 = st.columns(2)

# 1. Bar Chart (Matplotlib)
with col1:
    st.subheader(f"1. {selected_player} Stats Bar Chart")
    fig, ax = plt.subplots()
    ax.bar(df['Category'], df['Stats'], color=['#3b7bbf', '#f7a600', '#2a9d8f', '#e63946', '#f1faee'])
    ax.set_ylabel('Stats')
    ax.set_title(f'{selected_player} Stats by Category')
    st.pyplot(fig)

# 2. Pie Chart (Plotly)
with col2:
    st.subheader(f"2. {selected_player} Stats Pie Chart")
    fig_pie = px.pie(df, values='Stats', names='Category', title=f'{selected_player} Stats Distribution')
    st.plotly_chart(fig_pie)

# Layout for other charts
col3, col4 = st.columns(2)

# 3. Line Chart (Matplotlib)
with col3:
    st.subheader(f"3. {selected_player} Stats Line Chart")
    fig_line, ax = plt.subplots()
    ax.plot(df['Category'], df['Stats'], marker='o', color='#1c3b65')
    ax.set_ylabel('Stats')
    ax.set_title(f'{selected_player} Stats by Category (Line Chart)')
    st.pyplot(fig_line)

# 4. Scatter Plot (Plotly)
with col4:
    st.subheader(f"4. {selected_player} Stats Scatter Plot")
    fig_scatter = px.scatter(df, x="Category", y="Stats", color="Category", title=f"{selected_player} Stats Scatter Plot")
    st.plotly_chart(fig_scatter)

# Layout for the last chart
st.subheader(f"5. {selected_player} Stats Area Chart")
fig_area = px.area(df, x="Category", y="Stats", title=f"{selected_player} Stats Area Chart")
st.plotly_chart(fig_area)
