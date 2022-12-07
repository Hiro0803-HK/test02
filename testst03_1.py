# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:51:05 2022

@author: 0H06015 小木曽　弘朗
"""
import streamlit as st
#import numpy as np
#import pandas as pd
from PIL import Image
import time
inport time

st.title('グループ制作サンプル')

PAGE = st.sidebar.selectbox(
    "ページ選択", ["ページ1", "ページ2"], 
    key="page-select"
    )

YBCList = ["瘦せ型", "普通", "ふくよか"]

TList = ["やや低め", "平均程度", "高め"]

HSList = ["短め", "普通", "長め"]

WJList = ["きれい目", "アメカジ", "ストリート", "トラッド", "ワーク", "サーフ"]

st.markdown(
"""
<style>
div[data-baseweb = "popover"] ul {
    background-color:#7086ba;
}
div.st-bh{
    background-color:#239ba6;
}
div.st-b8{
    background-color:blue
}

</style>
""", unsafe_allow_html=True)

def page1():
    
       def change_page():
            
            st.session_state["page-select"] = "ページ2"
    
       with st.form(key="my_form01"):
    
        st.radio("あなたの体型は", YBCList, key="ybc")

        st.write(st.session_state["ybc"])
        
        st.radio("あなたの身長は？", TList, key="ytl")
        
        st.radio("あなたの髪型は？", HSList, key="yhs")
        
        st.selectbox("あなたの好きなジャンルは？", WJList, key="lwj")
            
        if st.form_submit_button("ジャンルの説明の表示/更新"):
            def JInfo():
                    with st.expander(f'**{st.session_state["lwj"]}**とは？'):
                        st.markdown(f'**{st.session_state["lwj"]}**というジャンルは')
                        st.markdown('<span style = "color:yellow;">--------ここにジャンルの説明--------</span>', unsafe_allow_html=True)
        
            JInfo()
        st.form_submit_button(label = "決定", on_click = change_page)

def page2():
        
        def change_page():
            
             st.session_state["page-select"] = "ページ1"
            
        with st.form(key="my_form01"):

           nybc = st.session_state["ybc"]
           nytl = st.session_state["ytl"]
           nyhs = st.session_state["yhs"]
           nywj = st.session_state["lwj"]

           LC = [nybc, nytl, nyhs, nywj]

           YLC = '_'.join(LC)

           st.write(f'体型が{nybc}で身長が{nytl}で髪型が{nyhs}で{nywj}が好きな人は')
        
           st.write(YLC + "(画像のパス)")
           
           #time.sleep(3)
           #st.image(f'{YLC}.png')
        
           st.form_submit_button(label = "戻る", on_click = change_page)
    
        






if PAGE == "ページ1":
    page1()
    
elif PAGE == "ページ2":
    page2()






