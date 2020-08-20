import streamlit as st
import pandas as pd
import pandas_dedupe
import base64
from io import BytesIO
#load dataframe
st.set_option('deprecation.showfileUploaderEncoding', False)
st.title('Deduplication of Data')
new_list = []
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")


if uploaded_file is not None:
  df = pd.read_csv('newt.csv')
  for col in df.columns:
    new_list.append(col)
  options = st.multiselect('Select the multiple columns which u need to check duplicates',new_list )
  if st.button('Deduplicate'):
    df_final = pandas_dedupe.dedupe_dataframe(df,options)
    st.dataframe(df_final)
  
