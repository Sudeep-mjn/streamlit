import streamlit as st 
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="app",page_icon="😎",layout="wide"
)

st.title("Excell data Read and Display")
st.write('DATA')

@st.cache_data
def load_data(path: str):
    data = pd.read_excel(path)
    return data

uploaded_file = st.sidebar.file_uploader("Choose  a file")

if uploaded_file is None:
    st.info("upload a file through config" , icon="😎")
    st.stop()
else:
    df = load_data(uploaded_file)
    with st.expander("Data Preview"):
         st.dataframe(df)


# def plot_bottom_left():
#     sales_data = df(

#         fig = st.line(
#             sales_data,
#             x="Annual salary",
#             y="Age",
#             color = "Scenario",
#         )
#         st.plotly_chart(fig, use_container_width=True)
#     )
# plot_bottom_left()







# if "my_input" not in st.session.state:
#     st.session_state["my_input"] =""

# my_input = st.text_input("Input a text here", st.session_state["my_input"])
# submit = st.button("Submit")
# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("you have entered",my_input)