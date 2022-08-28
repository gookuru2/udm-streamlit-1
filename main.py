import streamlit as st
import numpy as np
import pandas as pd 
# from PIL import Image

# --------------------------------
# 基本的な使い方
# --------------------------------

st.title('streamit 入門')

st.write('DataFrame')

df = pd.DataFrame({
   '1列目':[1,2,3,4] ,
   '2列目':[10,20,30,40] 
})

st.write(df)
st.dataframe(df.style.highlight_max(axis=0),width=800,height=300)
st.table(df)

"""
# level1
## level2
### level3
```python
import streamlit as st
import numpy as np
import pandas as pd 
```
"""

df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns = ['a','b','c']
)
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns = ['lat','lon']
)
st.dataframe(df3)
st.map(df3)


# --------------------------------
# インタラクティブなウィジェット
# --------------------------------
st.write('Interactive Widgets')

## チェックボックス
if st.checkbox('Show Image'):
  img = Image.open('test.jpg')
  st.image(img,caption='vegitables',use_column_width=True)

## セレクトボックス
option = st.selectbox(
    'あなたが好きな数字を教えてください　',
    list(range(1,11))
)
'あなたの好きな数字は ', option,  'です'

## テキストボックス
#hobby = st.text_input('あなたの趣味を教えてください')
#'あなたの趣味は',hobby,'です'

## スライダー
#condition = st.slider('あなたの今の調子は',0,100,50)
#'あなたのコンディションは',condition,'です'

# --------------------------------
# レイアウトを整える
# --------------------------------

## サイドバー
hobby2 = st.sidebar.text_input('あなたの趣味を教えてください')
condition2 = st.sidebar.slider('あなたの今の調子は',0,100,50)

'あなたの趣味は',hobby2,'です'
'あなたのコンディションは',condition2,'です'

## 2columns
left_column,right_column = st.columns(2)
button = left_column.button('右にボタンを表示') 
if button:
   right_column.write('ここは右カラム')

## beta_expander
expander1 = st.expander('問い合わせ1') 
expander1.write('問い合わせ内容を書く')
expander2 = st.expander('問い合わせ2') 
expander2.write('問い合わせ内容を書く')
expander3 = st.expander('問い合わせ3') 
expander3.write('問い合わせ内容を書く')


## プログレスバーの表示
import time
st.write('プログレスバーの表示')
'Start !'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
   latest_iteration.text(f'Iteration{i+1}')
   bar.progress(i+1)
   time.sleep(0.1)
'Done !'






