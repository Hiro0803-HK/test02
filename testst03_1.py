# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:51:05 2022

@author: 0H06015 小木曽　弘朗
"""
import streamlit as st
#import numpy as np
#import pandas as pd
from PIL import Image

st.title('マイクロゼット')

PAGE = st.sidebar.selectbox(
    "ページ選択", ["ページ1", "ページ2","ページ3"], 
    key="page-select"
    )

YBCList = ["瘦せ型　　　　　　　　　　", "普通　　　　　　　　　　", "がっちり"] 

cont = st.container()
cont2 = st.container()
cont3 = st.container()
cont4 = st.container()

colp2_01, colp2_02, colp2_03 = cont.columns([0.1, 6, 0.1])
colp1_01, colp1_02, colp1_03 = cont2.columns(3)
colp4_01, colp4_02, colp4_03 = cont3.columns([0.1, 6, 0.1])
colp3_01, colp3_02, colp3_03 = cont4.columns(3)
pg3_col01, pg3_col02, pg3_col03 = st.columns(3)

Col01 = [colp1_01, colp1_02, colp1_03]
Col02 = [colp3_01, colp3_02, colp3_03]

TList = ["やや低め", "平均程度", "高め"]

IMList = ["清楚", "クール", "明るめ", "大人","渋い"]

YSize = ["とてもぴったり", "ぴったり", "少しぴったり", "普通", "少しゆったり", "ゆったり", "とてもゆったり"]

YMsk = ["白", "黒", "グレー", "ベージュ", "茶色", "青", "紺", "ピンク", "緑"]

WJList = ["きれい目", "アメカジ", "ストリート", "トラッド", "ワーク", "サーフ"]

wear01 = ["Tシャツ", "スウェット", "ジャケット", "パーカー", "セーター", "カーディガン", "コート", "ダウンジャケット", "シャツ", "ポロシャツ", "タートルネック"]

wear02 = {"ジーパン":5, "チノパン":5, "スウェットパンツ":3, "カーゴパンツ":4, "スラックス":4, "イージーパンツ":5, "スキニー":6, "フレアパンツ":7, "ショートパンツ":8, "ジョガーパンツ":9, "コーディルー":10, "レザーパンツ":11}


st.markdown(
"""
<style>
div[data-baseweb = "popover"] ul {
    background-color:#7086ba;
}
div.st-bh{
    background-color:#239ba6;
}

</style>
""", unsafe_allow_html=True)

#nwear = [fuku for fuku, score in wear02.items() if score == 5]

#st.write(nwear)

def page1():
    
       def change_page():
            
            st.session_state["page-select"] = "ページ2"
    
       st.slider("あなたの身長は？", 100, 200, 150, key="ytl")
       st.write("\n")

       st.write("あなたの体系は？")
       col1,col2,col3 = st.columns(3)     
       with col1:
           image = Image.open('ほっそり.png')
           st.image(image,width=70)
           
       with col2:
           image = Image.open('標準.png')
           st.image(image,width=82)
     
       with col3:
           image = Image.open('がっちり.png')
           st.image(image,width=100)

        
           
       
 
           
       st.radio("　", YBCList, key="ybc",horizontal=True)
       st.write("\n")
 
       
       st.radio("あなたの目指す雰囲気は？", IMList, key="yhs", horizontal=True)
       st.write("\n")
        
      # st.write("ここに画像挿入")

       st.select_slider("あなたの着たいサイズ感は？", YSize, YSize[3], key="ysz")
       st.write("\n")
       
       
       st.selectbox("あなたの好きなマスクの色は？", YMsk, key="Ymk")
       st.write("\n")
            
      
        
       st.button(label = "決定", on_click = change_page)
      
def page2():
        
     def change_page():
        
         st.session_state["page-select"] = "ページ1"
            
     def next_page():
        
         st.session_state["page-select"] = "ページ3"

     with colp2_01:
            st.empty()

     with colp2_02:

            st.multiselect("あなたの好きな上の服は", wear01, key="Lwear01")
            YLW = st.session_state["Lwear01"]

     with colp2_03:

            st.empty()
     try:

         i = 0
         cnt = 0
         while(True):

            with Col01[cnt]:
                st.write(YLW[i])
            
            cnt = cnt + 1
            i = i + 1
            if cnt > 2:
                cnt = 0

     except IndexError:
            st.empty()
            
     with colp4_01:
            st.empty()

     with colp4_02:
            st.multiselect("あなたの好きな下の服は", wear02, key="Lwear02")
            YLP = st.session_state["Lwear02"]
     with colp4_03:
            st.empty()
     try:
         i = 0
         cnt = 0
         while(True):

            with Col02[cnt]:
                st.write(YLP[i])
            
            cnt = cnt + 1
            i = i + 1
            if cnt > 2:
                cnt = 0

     except IndexError:
        st.empty()

     st.button(label = "戻る", on_click = change_page)
     st.button(label = "次へ", on_click = next_page)

        
def page3():
    
    def change_page():
                
          st.session_state["page-select"] = "ページ1"
        
    image = Image.open('IMG_7837 (2).PNG')

    with pg3_col01:
            st.write("あなたに似合う服の系統は")

    with pg3_col02:
            st.empty()  


    with pg3_col03:
            st.header("ストリート")
            st.image(image, caption='IMG_7837 (2).PNG',use_column_width=True)

        
         
         
         
    st.button(label = "戻る", on_click = change_page)
    

if PAGE == "ページ1":
    page1()
    
elif PAGE == "ページ2":
    page2()
    
elif PAGE == "ページ3":
    page3()

