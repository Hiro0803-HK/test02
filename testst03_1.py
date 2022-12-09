# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:51:05 2022

@author: 0H06015 小木曽　弘朗
"""
import streamlit as st
#import numpy as np
#import pandas as pd
from PIL import Image
#import time

st.title('グループ制作サンプル')

PAGE = st.sidebar.selectbox(
    "ページ選択", ["ページ1", "ページ2"], 
    key="page-select"
    )

YBCList = ["瘦せ型", "普通", "ふくよか"] 

TList = ["やや低め", "平均程度", "高め"]

IMList = ["清楚", "クール", "明るめ", "大人", "05"]

YSize = ["とてもぴったり", "ぴったり", "少しぴったり", "普通", "少しゆったり", "ゆったり", "とてもゆったり"]

YMsk = ["黒", "白", "グレー", "紺", "青", "茶色", "ピンク", "緑", "ベージュ"]

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
    
       with st.form(key="my_form01"):
    
        st.slider("あなたの身長は？", 100, 200, 150, key="ytl")
        
        st.radio("あなたの体型は", YBCList, key="ybc")
        
        st.radio("あなたの目指す雰囲気は？", IMList, key="yhs")

        st.select_slider("あなたの着てみたいサイズ感は", YSize, YSize[3], key="ysz")  

        st.selectbox("あなたの好きなマスクの色は", YMsk, key="Ymk")
      
        st.form_submit_button(label = "決定", on_click = change_page)

def page2():
        
        def change_page():
            
             st.session_state["page-select"] = "ページ1"
            
        with st.form(key="my_form01"):

             st.multiselect("あなたの好きな服は")


           st.form_submit_button(label = "戻る", on_click = change_page)
    
        






if PAGE == "ページ1":
    page1()
    
elif PAGE == "ページ2":
    page2()






