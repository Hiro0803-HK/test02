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

st.image(Image.open('micloset.png'))

PAGE = st.sidebar.selectbox(
    "ページ選択", ["ページ1", "ページ2","ページ3"], 
    key="page-select"
    )

YBCList = ["細身　　　　　　　　　　　", "普通　　　　　　　　　　", "筋肉質"] 

cont = st.container()
cont2 = st.container()
cont3 = st.container()
cont4 = st.container()
cont5 = st.container()
cont6 = st.container()
cont7 = st.container()
cont8 = st.container()

colp2_01, colp2_02, colp2_03 = cont.columns([0.1, 6, 0.1])
colp1_01, colp1_02, colp1_03 = cont2.columns(3)
colp4_01, colp4_02, colp4_03 = cont3.columns([0.1, 6, 0.1])
colp3_01, colp3_02, colp3_03 = cont4.columns(3)
pg3_col01, pg3_col02, pg3_col03 = cont5.columns([2.4, 6, 0.1])
colp5_01, colp5_02, colp5_03 = cont6.columns(3)
pg7_col01, pg7_col02, pg7_col03 = cont7.columns([2.4, 6, 0.1])
colp6_01, colp6_02, colp6_03 = cont8.columns(3)

Col01 = [colp1_01, colp1_02, colp1_03]
Col02 = [colp3_01, colp3_02, colp3_03]
Col03 = [colp5_01, colp5_02, colp5_03]
Col04 = [colp6_01, colp6_02, colp6_03]

TList = ["やや低め", "平均程度", "高め"]

IMList = ["清楚", "クール", "明るめ", "大人","渋め", "シンプル"]

YSize = ["とてもぴったり", "ぴったり", "少しぴったり", "普通", "少しゆったり", "ゆったり", "とてもゆったり"]

YMsk = ["白", "黒", "グレー", "ベージュ", "ピンク", "緑"]

WJlist = ["きれい目", "アメカジ", "ストリート", "トラッド", "ワーク", "ロック", "アウトドア＆スポーツ"]

wear01 = ["Tシャツ", "スウェット", "ジャケット", "パーカー", "セーター", "カーディガン", "コート", "ダウンジャケット", "シャツ", "ポロシャツ", "タートルネック", "ベスト"]

wear02 = ["ジーパン", "チノパン", "スウェットパンツ", "カーゴパンツ", "スラックス", "イージーパンツ", "スキニー", "フレアパンツ", "ショートパンツ", "ジョガーパンツ", "レザーパンツ", "トラックパンツ", "コーデュロイパンツ"]

#きれいめ　#パーカー、ポロシャツ
CCCC = {"きれい目" : {"Tシャツ":5, "スウェット":3, "ジャケット":3, "パーカー":4, "セーター":5, "カーディガン":4, "コート":5, "ダウンジャケット":4, "シャツ":5, "ポロシャツ":4, "タートルネック":3},
        "アメカジ" : {"Tシャツ":5, "スウェット":4, "ジャケット":5, "パーカー":5, "カーディガン":2, "シャツ":5, "ポロシャツ":3},
        "トラッド" : {"Tシャツ":3, "ジャケット":5, "セーター":4, "カーディガン":2, "コート":5, "ポロシャツ":5, "タートルネック":1, "ベスト":5},
        "ワーク" : {"ダウンジャケット":5, "ジャケット":5, "シャツ":4, "タートルネック":5},
        "ロック" : {"Tシャツ":10, "ジャケット":5, "セーター":1, "シャツ":2, "ポロシャツ":3},
        "アウトドア＆スポーツ" : {"Tシャツ":5, "ジャケット":4, "パーカー":5, "ダウンジャケット":5},
        "ストリート" : {"Tシャツ":5, "スウェット":5, "ジャケット":4, "パーカー":5, "ダウンジャケット":3, "ポロシャツ":3, "タートルネック":2}
        }

DDDD = {"きれい目" : {"ジーパン":4, "チノパン":5, "スウェットパンツ":3, "スラックス":5, "イージーパンツ":4, "スキニー":2, "フレアパンツ":3, "コーデュロイパンツ":4},
        "アメカジ" : {"ジーパン":5, "チノパン":4, "スウェットパンツ":1, "カーゴパンツ":3, "スキニー":2},
        "ストリート" : {"トラックパンツ":4, "ジーパン":5, "チノパン":3, "スウェットパンツ":4, "カーゴパンツ":5, "イージーパンツ":1, "ショートパンツ":4, "ジョガーパンツ":2},
        "トラッド" : {"ジーパン":4, "チノパン":5, "スラックス":5, "イージーパンツ":5, "スキニー":1, "ジョガーパンツ":2},
        "ワーク" : {"ジーパン":5, "チノパン":5, "カーゴパンツ":3, "イージーパンツ":4, "スキニー":2, "ジョガーパンツ":1},
        "ロック" : {"ジーパン":4, "カーゴパンツ":2, "スキニー":5, "レザーパンツ":5},
        "アウトドア＆スポーツ" : {"ジーパン":2, "チノパン":3, "スウェットパンツ":4, "カーゴパンツ":4, "イージーパンツ":2, "ショートパンツ":8, "ジョガーパンツ":5, "トラックパンツ":5},
        }


Users = {} #空の辞書型の変数

IMGLIST01 = []

IMGLIST02 = []

IMGNAME = []

st.markdown(
"""
<style>

div[data-baseweb = "popover"] ul {
    background-color:#7086ba;
}

</style>
""", unsafe_allow_html=True)

# div.st-bh{
#     background-color:white;
# }
#[data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
#        width: 500px;
#    }
# [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
#        width: 500px;
#        margin-left: -500px;
#    }


def warning(url):
     st.markdown(f'<p style="background-color:#ea5419;color:white;font-size:40px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)

def wegets(Rtext):
     st.markdown(f'<p style="background-color:#F8B800;color:black;font-size:20px;border-radius:2%;">{Rtext}</p>', unsafe_allow_html=True)


#nwear = [fuku for fuku, score in wear02.items() if score == 5]

#st.write(nwear)

def AAAA(arr, dict):

    Keys = dict.keys()

    Score = 0

    for x in arr:
        for y in Keys:
            if x == y:
                Score = Score + dict[x]
            
    return Score
            
def Genre_System():
        try:
            UsersData01 = st.session_state["Lwear01"]
            UsersData02 = st.session_state["Lwear02"]
            UsersBC = st.session_state["ybc"]

           
#######################################################################################身長と体型
            if st.session_state["ytl"] <= 165:

                WJlist.remove("トラッド")
                WJlist.remove("きれい目")
                WJlist.remove("ロック")
               
                if UsersBC ==  "細身　　　　　　　　　　　":

                    WJlist.remove("アメカジ")
                    WJlist.remove("ワーク")          
       
            elif st.session_state["ytl"] > 165 and st.session_state["ytl"] < 175:

                WJlist.remove("ロック")
                
                
                if UsersBC ==  "細身　　　　　　　　　　　":

                    WJlist.remove("アメカジ")
                    WJlist.remove("ワーク")

                elif UsersBC ==  "筋肉質":

                    WJlist.remove("きれい目")
                    WJlist.remove("トラッド")

                               

            elif st.session_state["ytl"] >= 175:
                

                
                    
                if UsersBC ==  "細身　　　　　　　　　　　":

                        WJlist.remove("アメカジ")
                        WJlist.remove("ワーク")
        
                elif UsersBC == "筋肉質":

                        WJlist.remove("きれい目")
                        WJlist.remove("トラッド")
            
###########################################################################################

            if st.session_state["yhs"] =="清楚":

                Users = [i for i in WJlist if i == "きれい目" or i == "トラッド"]

                
            
            elif st.session_state["yhs"] =="クール":
                       
                Users = [i for i in WJlist if i == "きれい目" or i == "ストリート"]

                
            
            elif st.session_state["yhs"] =="大人":
                
                Users = [i for i in WJlist if i == "ワーク" or i == "トラッド"]

            elif st.session_state["yhs"] =="明るめ":

                Users = [i for i in WJlist if i == "アメカジ"  or i == "アウトドア＆スポーツ"]
            
            elif st.session_state["yhs"] =="渋め":
                
                Users = [i for i in WJlist if i != "きれい目" and i != "ストリート"]
                
            
            elif st.session_state["yhs"] =="シンプル":
                        
                Users = [i for i in WJlist if i == "きれい目" or i == "トラッド" or i == "アメカジ"]


            if len(Users) == 0:
                warning("その情報に合った服の系統はありません")
              
            
            else:
                Result = 0
                Result02 = 0

                for Name in Users:

                        #st.write(AAAA(UsersData02, DDDD[Name]))

                        if Result < AAAA(UsersData01, CCCC[Name]):
                            Result = AAAA(UsersData01, CCCC[Name])
                            Rname = Name
                        
                        if Result02 < AAAA(UsersData02, DDDD[Name]):
                            Result02 = AAAA(UsersData02, DDDD[Name])
                            Rname02 = Name

                RWEARS01 = [fuku for fuku, score in CCCC[Rname].items() if score >= 4]
                
                for x in RWEARS01:
                    
                    IMGLIST01.append(f'{Rname}_{x}')
            
                RWEARS02 = [fuku for fuku, score in DDDD[Rname02].items() if score >= 4]
               
                for x in RWEARS02:
                    
                    IMGLIST02.append(f'{Rname02}_{x}')

                IMGNAME.append(Rname)
                IMGNAME.append(Rname02)

                """
                #### あなたに似合う服のジャンルは

                """

                #st.write("上の服：" + Rname)
                #st.write()
                #st.write("下の服：" + Rname02)
             
                
        except KeyError:
            st.empty()
        except IndexError:
            st.empty()
        except UnboundLocalError:
            #st.write('<span style="color:yellow;background:green">何も選択されていません</span>', unsafe_allow_html=True)
            warning("何も選択されていません")


def page1():
    
    

       def change_page():
            
            st.session_state["page-select"] = "ページ2"
       wegets("あなたの身長は？")
       st.slider("　", 100, 200, 150, key="ytl")
       st.write("\n")

       wegets("あなたの体型は？")
       col1,col2,col3 = st.columns(3)     
       with col1:
           image = Image.open('ほっそり.png')
           st.image(image,width=75)
           
       with col2:
           image = Image.open('標準.png')
           st.image(image,width=82)
     
       with col3:
           image = Image.open('がっちり.png')
           st.image(image,width=100)

        
           
       
 
           
       st.radio("　", YBCList, key="ybc",horizontal=True)
       st.write("\n")
 
       wegets("あなたの目指す雰囲気は？")
       st.radio("　", IMList, key="yhs", horizontal=True)
       st.write("\n")
        
    
       wegets("あなたの着たいサイズ感は？")
       st.select_slider("　", YSize, YSize[3], key="ysz")
       st.write("\n")
       
       wegets("あなたの好きなマスクの色は？")
       st.selectbox("　", YMsk, key="Ymk")
       st.write("\n")
            
      
        
       st.button(label = "決定", on_click = change_page)
      
def page2():

    
     st.session_state["ytl"] = st.session_state["ytl"]
     st.session_state["ybc"] = st.session_state["ybc"]
     st.session_state["yhs"] = st.session_state["yhs"]
     st.session_state["ysz"] = st.session_state["ysz"]
     st.session_state["Ymk"] = st.session_state["Ymk"]
     
   
     def change_page():
        
         st.session_state["page-select"] = "ページ1"
            
     def next_page():
        
         st.session_state["page-select"] = "ページ3"

     with colp2_01:

            st.empty()
            
     with colp2_02:
            wegets("あなたの好きなトップスは")
            st.multiselect("　", wear01, key="Lwear01")

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
            wegets("あなたの好きなボトムスは")
            st.multiselect("　", wear02, key="Lwear02")
            
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
        
   
    with pg3_col01:
            st.empty()
           #st.write("AAA")

    with pg3_col02:
            
        try:

            Genre_System()
            st.write(f'<span style="color:black;font-size:20px;">あなたにはトップスなら</span><span style="color:#5406d1;font-size:27px;">{IMGNAME[0]}</span><span style="color:black;font-size:20px;">が似合うはずです</span>', unsafe_allow_html=True)

            if IMGNAME[0] == "きれい目":
                with st.expander(f'{IMGNAME[0]}の説明'):
                    """
                    ###### 過度なデザインのものではなく、
                    ###### すっきりとした配色やアイテムを
                    ###### 揃えたものです
                    """
            elif IMGNAME[0] == "トラッド":
                with st.expander(f'{IMGNAME[0]}の説明'):
                    """
                    ###### トラッドとは、
                    ###### 「伝統的な」「保守的な」を意味する「トラディショナル」の和製英語で
                    ###### 源流は英国紳士服です
                    ###### 定番はスリーピース（ジャケット、ベスト、パンツの組み合わせ）です。

                    """
            elif IMGNAME[0] == "アメカジ":
                with st.expander(f'{IMGNAME[0]}の説明'):
                    """
                    ###### アメカジとは、
                    ###### 「アメリカンカジュアル」の略称で
                    ###### アメリカ風の服でラフ過ぎないキッチリとした着こなしのことです

                    """
            elif IMGNAME[0] == "ストリート":
                with st.expander(f'{IMGNAME[0]}の説明'):
                    """
                    ###### ストリートとは、
                    ###### 若者の間で自然発生した自由な着こなしのことです
                    ###### オーバーサイズのスウェット、パーカー、ジーンズ等を
                    ###### 合わせたラフなスタイルが代表的です。

                    """
            elif IMGNAME[0] == "サーフ":
                with st.expander(f'{IMGNAME[0]}の説明'):
                    """
                    ###### サーファーをイメージした
                    ###### ラフでカジュアルなスタイルのことです。
                    ###### 

                    """
            elif IMGNAME[0] == "ワーク":
                with st.expander(f'{IMGNAME[0]}の説明'):
                    """
                    ###### ワークとは、
                    ###### 労働者の作業着を着こなすスタイルであり、無骨で実用的、
                    ###### シンプルで男らしいファッションです。
                    ###### ワーク系のアイテムばかりでコーディネートしたときにワイルドすぎると感じる場合は、
                    ###### きれいめのアイテムを取り入れるのがおすすめです。

  
                    """
            elif IMGNAME[0] == "アウトドア＆スポーツ":
                with st.expander(f'{IMGNAME[0]}の説明'):
                    """
                    ###### アウトドア＆スポーツとは、
                    ###### 動きやすさ、機能性を軸にして
                    ###### 日常に落とし込んだアイテムの組み合わせの
                    ###### スタイルのことです。

                    """
            elif IMGNAME[0] == "ロック":
                with st.expander(f'{IMGNAME[0]}の説明'):
                    """
                    ###### ロック系とは、
                    ###### 元々はロックミュージシャンが着ていたスタイルで、
                    ###### 時代によって定義が変わっていくファッションです。
                    ###### 現在では黒を基調とし、革素材を使用するのがメジャーなスタイルです。

                    """

        except IndexError:
            warning("別の選択肢を試してみてください")
                 
                           
    with pg3_col03:
           st.empty()

    try:
        
        i = 0
        cnt = 0
        while(True):

            with Col03[cnt]:
                
                try:
                    image = Image.open(f'{IMGNAME[0]}/{IMGLIST01[i]}.png')
                    st.image(image, caption=IMGLIST01[i])
                except FileNotFoundError:
                    EMP = Image.open(f'{IMGNAME[0]}/{IMGNAME[0]}_empty.png')
                    st.image(EMP, caption=IMGLIST01[i])
                
            cnt = cnt + 1
            i = i + 1
            if cnt > 2:
                cnt = 0

    except IndexError:
            st.empty()

    
    with pg7_col01:
            st.empty()
           #st.write("AAA")

    with pg7_col02:
            
        try:

            st.write(f'<span style="color:black;font-size:20px;">あなたにはボトムスなら</span><span style="color:#5406d1;font-size:27px;">{IMGNAME[1]}</span><span style="color:black;font-size:20px;">が似合うはずです</span>', unsafe_allow_html=True)

            if IMGNAME[1] == "きれい目":
                with st.expander(f'{IMGNAME[1]}の説明'):
                    """
                    ###### 過度なデザインのものではなく、
                    ###### すっきりとした配色やアイテムを
                    ###### 揃えたものです
                    """
            elif IMGNAME[1] == "トラッド":
                with st.expander(f'{IMGNAME[1]}の説明'):
                    """
                    ###### トラッドとは、
                    ###### 「伝統的な」「保守的な」を意味する「トラディショナル」の和製英語で
                    ###### 源流は英国紳士服です
                    ###### 定番はスリーピース（ジャケット、ベスト、パンツの組み合わせ）です。

                    """
            elif IMGNAME[1] == "アメカジ":
                with st.expander(f'{IMGNAME[1]}の説明'):
                    """
                    ###### アメカジとは、
                    ###### 「アメリカンカジュアル」の略称で
                    ###### アメリカ風の服でラフ過ぎないキッチリとした着こなしのことです

                    """
            elif IMGNAME[1] == "ストリート":
                with st.expander(f'{IMGNAME[1]}の説明'):
                    """
                    ###### ストリートとは、
                    ###### 若者の間で自然発生した自由な着こなしのことです
                    ###### オーバーサイズのスウェット、パーカー、ジーンズ等を
                    ###### 合わせたラフなスタイルが代表的です。

                    """
            elif IMGNAME[1] == "サーフ":
                with st.expander(f'{IMGNAME[1]}の説明'):
                    """
                    ###### サーファーをイメージした
                    ###### ラフでカジュアルなスタイルのことです。
                    ###### 

                    """
            elif IMGNAME[1] == "ワーク":
                with st.expander(f'{IMGNAME[1]}の説明'):
                    """
                    ###### ワークとは、
                    ###### 労働者の作業着を着こなすスタイルであり、無骨で実用的、
                    ###### シンプルで男らしいファッションです。
                    ###### ワーク系のアイテムばかりでコーディネートしたときにワイルドすぎると感じる場合は、
                    ###### きれいめのアイテムを取り入れるのがおすすめです。

                    """
            elif IMGNAME[1] == "アウトドア＆スポーツ":
                with st.expander(f'{IMGNAME[1]}の説明'):
                    """
                    ###### アウトドア＆スポーツとは、
                    ###### 動きやすさ、機能性を軸にして
                    ###### 日常に落とし込んだアイテムの組み合わせの
                    ###### スタイルのことです。

                    """
            elif IMGNAME[1] == "ロック":
                with st.expander(f'{IMGNAME[1]}の説明'):
                    """
                     ###### ロック系とは、
                     ###### 元々はロックミュージシャンが着ていたスタイルで、
                     ###### 時代によって定義が変わっていくファッションです。
                     ###### 現在では黒を基調とし、革素材を使用するのがメジャーなスタイルです。

                    """
            
            
        except IndexError:
            warning("別の選択肢を試してみてください")
       
                           
    with pg7_col03:
           st.empty()

    try:
        
        i = 0
        cnt = 0
        while(True):

            with Col04[cnt]:

               try:
                    image = Image.open(f'{IMGNAME[1]}/{IMGLIST02[i]}.png')
                    st.image(image, caption=IMGLIST02[i])
               except FileNotFoundError:
                    EMP = Image.open(f'{IMGNAME[1]}/{IMGNAME[1]}_empty.png')
                    st.image(EMP, caption=IMGLIST02[i])
                 
            cnt = cnt + 1
            i = i + 1
            if cnt > 2:
                cnt = 0

    except IndexError:
            st.empty()
    
    with st.sidebar:
        mask = st.session_state["Ymk"]

        st.image(Image.open(f'マスク/{mask}.png'), caption=f'あなたが選んだマスクの色：{mask}' , width=200)
        #if mask == "白":
        #    imagem = Image.open('白.png')
        #    st.image(imagem,width=250)
        #elif mask == "黒":
        #    imagem = Image.open('黒.png')
        #    st.image(imagem,width=250)
        #elif mask == "グレー":
        #    imagem = Image.open('グレー.png')
        #    st.image(imagem,width=250)
        #elif mask == "ベージュ":
        #    imagem = Image.open('ベージュ.png')
        #    st.image(imagem,width=250)
        #elif mask == "ピンク":
        #    imagem = Image.open('ピンク.png')
        #    st.image(imagem,width=250)   
        #elif mask == "緑":
        #    imagem = Image.open('緑.png')
        #    st.image(imagem,width=250)
         
         
    st.button(label = "戻る", on_click = change_page)


if PAGE == "ページ1":
    page1()
    
elif PAGE == "ページ2":
    page2()
    
elif PAGE == "ページ3":
    page3()

