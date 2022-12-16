# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:51:05 2022

@author: 0H05008 音澤璃空
"""
import streamlit as st
from PIL import Image


st.title('マイクロゼット')

PAGE = st.sidebar.selectbox(
    "ページ選択", ["ページ1", "ページ2","ページ3"], 
    key="page-select"
    )

YBCList = ["瘦せ型　　　　　　　　　　", "普通　　　　　　　　　　", "がっちり"] 

colp1_01, colp1_02, colp1_03 = st.columns(3)

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
            





        st.button(label = "戻る", on_click = change_page)
        st.button(label = "次へ", on_click = next_page)
    
        
def page3():
    
    def change_page():
        
        st.session_state["page-select"] = "ページ1"
        

    st.write("結果表示")





if PAGE == "ページ1":
    page1()
    
elif PAGE == "ページ2":
    page2()
    
elif PAGE == "ページ3":
    page3()


