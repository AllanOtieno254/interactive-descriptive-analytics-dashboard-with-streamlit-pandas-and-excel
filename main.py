import streamlit as st
import pandas as pd
import plotly.express as px
import time
from streamlit_option_menu import option_menu
from numerize import numerize

# --- Page Config ---
st.set_page_config(
    page_title="Descriptive Data Analysis Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
)

# --- Embedded Custom CSS ---
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f7f9fc;
        color: #333;
    }
    .css-1d391kg { background-color: #f0f2f6; }
    .css-1n76uvr { color: #333; }
    h1, h2, h3 {
        color: #004080;
    }
    .stMetric {
        background-color: #121720;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.1);
    }
    .stDataFrame {
        background-color: #fff;
        border-radius: 10px;
        padding: 10px;
    }
    .streamlit-expanderHeader {
        font-size: 16px;
        color: #003366;
    }
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #00cc66 , #ffcc00);
    }
    .footer {
        text-align: center;
        color: #888;
        font-size: 13px;
        padding: 20px 0;
    }
    .js-plotly-plot .plot-title {
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Load dataset ---
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

# --- Sidebar Navigation Menu ---
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Progress"],
        icons=["house", "bar-chart-line"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical"
    )

    st.header("Please Filter Here! 😊")
    region = st.multiselect(
        "Select the Region:", options=df["Region"].unique(), default=df["Region"].unique()
    )
    location = st.multiselect(
        "Select the Location:", options=df["Location"].unique(), default=df["Location"].unique()
    )
    construction = st.multiselect(
        "Select the Construction:", options=df["Construction"].unique(), default=df["Construction"].unique()
    )

df_selection = df.query("Region==@region & Location==@location & Construction==@construction")

# --- Homepage Function ---
def Homepage():
    with st.expander("My Database"):
        show_cols = st.multiselect(
            "Filter the Data Columns:",
            df_selection.columns,
            default=[
                "Policy", "Expiry", "Location", "State", "Region",
                "Investment", "Construction", "BusinessType", "Earthquake", "Flood", "Rating"
            ]
        )
        st.dataframe(df_selection[show_cols], use_container_width=True)

    total_investment = float(df_selection["Investment"].sum())
    investment_mode = float(df_selection["Investment"].mode()[0])
    investment_mean = float(df_selection["Investment"].mean())
    investment_median = float(df_selection["Investment"].median())
    rating_total = float(df_selection["Rating"].sum())

    total1, total2, total3, total4, total5 = st.columns(5, gap="large")
    with total1:
        st.info("Total Investment", icon="💰")
        st.metric(label="SUM KSH", value=f"{total_investment:,.0f}")
    with total2:
        st.info("Most Frequent Investment", icon="💰")
        st.metric(label="MODE KSH", value=f"{investment_mode:,.0f}")
    with total3:
        st.info("Average Investment", icon="💰")
        st.metric(label="MEAN KSH", value=f"{investment_mean:,.0f}")
    with total4:
        st.info("Investment Median", icon="💰")
        st.metric(label="MEDIAN KSH", value=f"{investment_median:,.0f}")
    with total5:
        st.info("Ratings", icon="📊")
        st.metric(label="Rating", value=numerize.numerize(rating_total, 2), help=f"Total Rating: {rating_total}")
    st.markdown("---")

# --- Graphs Function ---
def graphs():
    investment_by_business_type = (
        df_selection.groupby("BusinessType").count()[["Investment"]].sort_values(by="Investment")
    )

    fig_investment = px.bar(
        investment_by_business_type,
        x="Investment",
        y=investment_by_business_type.index,
        orientation="h",
        title="<b>Investment by Business Type</b>",
        color_discrete_sequence=["#0083B8"],
        template="plotly_white"
    )

    investment_state = df_selection.groupby("State").count()[["Investment"]]
    fig_state = px.line(
        investment_state,
        x=investment_state.index,
        y="Investment",
        title="<b>Investment by State</b>",
        color_discrete_sequence=["#0083b8"],
        template="plotly_white",
        markers=True
    )

    fig_state.update_layout(plot_bgcolor="rgba(0,0,0,0)", yaxis=dict(showgrid=False))
    fig_investment.update_layout(plot_bgcolor="rgba(0,0,0,0)", yaxis=dict(showgrid=False))

    left, right, center = st.columns(3)
    left.plotly_chart(fig_state, use_container_width=True)
    right.plotly_chart(fig_investment, use_container_width=True)

    with center:
        fig_pie = px.pie(
            df_selection,
            values='Rating',
            names='State',
            title='Ratings by Regions'
        )
        fig_pie.update_layout(legend_title="Regions", legend_y=0.9)
        fig_pie.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig_pie, use_container_width=True)

# --- Progress Bar Function ---
def Progressbar():
    target = 3_000_000_000  # Target amount
    current = df_selection["Investment"].sum()
    percent = round((current / target) * 100)
    mybar = st.progress(0)

    if percent > 100:
        st.subheader("🎯 Target Achieved!")
    else:
        st.write(f"You have achieved {percent}% of {format(target, ',d')} TZS")
        for i in range(percent):
            time.sleep(0.01)
            mybar.progress(i + 1, text=" Target Percentage")

# --- Main Logic ---
if selected == "Home":
    try:
        Homepage()
        graphs()
    except Exception as e:
        st.warning("⚠️ One or more options are mandatory or there's an error.")
        st.error(f"Details: {e}")

if selected == "Progress":
    try:
        Progressbar()
        graphs()
    except Exception as e:
        st.warning("⚠️ One or more options are mandatory or there's an error.")
        st.error(f"Details: {e}")

# --- Footer ---
st.markdown("---")
st.markdown("""
    <div class='footer'>
        <p>© 2025 <strong>Allan Otieno Akumu</strong>. All rights reserved.</p>
        <p>
            Built with ❤️ using <a href='https://streamlit.io/' target='_blank'>Streamlit</a> |
            <a href='https://github.com/AllanOtieno254' target='_blank'>GitHub</a> |
            <a href='https://www.linkedin.com/in/allan-otieno-b973a5251/' target='_blank'>LinkedIn</a>
        </p>
    </div>
""", unsafe_allow_html=True)
