import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time 
st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_interaction = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_interaction.text(f'Interaction{i+1}')
  bar.progress(i + 1)
  time.sleep(0.01)
'done!!'


left_column, right_column = st.beta_columns(2)
buttom = left_column.button('右カラムに文字を表示')
if buttom:
  right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容')
option = st.text_input('あなたの趣味を教えた下さい')
コンディション = st.slider('あなたの調子は?', 0, 100, 50)
'あなたの趣味は', option, 'です'
'あなたの調子は',コンディション
if st.checkbox('Show Image'):
  image = Image.open('sample.jpg')
  st.image(image, caption="junpei oda", use_column_width=True)


