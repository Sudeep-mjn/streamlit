import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="app", page_icon="😎", layout="wide"
)

st.title("Home Page")
st.write('DATA')

@st.cache_data
def load_data(path: str):
    data = pd.read_excel(path)
    return data

uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is None:
    st.info("Upload a file through the sidebar" , icon="😎")
    st.stop()
else:
    df = load_data(uploaded_file)
    with st.expander("Data Preview"):
        st.dataframe(df)

def plot_bottom_left():
    sales_data = df 

    fig = px.line(
        sales_data,
        x="AnnualSalary",
        y="Age",
        markers=True,
    )
    st.plotly_chart(fig, use_container_width=True)
plot_bottom_left()





# selected_item = st.multiselect(
#     "Column to use",
#     ["AnnualSalary", "Age"]
# )

def plot_gauge(
     indicator_number=1.99,
    indicator_color="#0068C9",
    indicator_suffix="%",
    indicator_title="Current Ratio",
    max_bound=3,
    ):
    
        fig = go.Figure(go.Indicator(
            domain = {'x': [0, 1], 'y': [0, 1]},
            value = 450,
            mode = "gauge+number+delta",
            title = {'text': "Speed"},
            delta = {'reference': 380},
            gauge = {'axis': {'range': [None, 500]},
                    'steps' : [
                        {'range': [0, 250], 'color': "lightgray"},
                        {'range': [250, 400], 'color': "gray"}],
                    'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}
                    )
                )

        fig.update_layout()
        st.plotly_chart(fig, use_container_width=True)

plot_gauge()

primaryColor = "#E694FF"

backgroundColor = "#001728"

textColor = "#FFF"

font = "sans serif"



def click_callback():
    st.session_state.button_clicked =True

button_clicked = st.button(
    "HELL00",
    key="greet_button",
    on_click = click_callback
)