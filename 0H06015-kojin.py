# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:52:54 2022

@author: 0H06015 小木曽　弘朗
"""

#形式は   xxx_xxx_xxx_00.txt または xxx_xxx_xxx_00.docx


import os
import shutil
import sys
import time


i = 0
flg = 0
try:
    def isint(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
            
    def isper(p, n):
        try:
            os.mkdir(os.path.join(p, n))
            os.rmdir(os.path.join(p, n))
            return True
        except PermissionError:
            return False
        except FileExistsError:
            return False
        
    def Valu(fl, sp):
        try:
            files[fl].split(sp)
            return True
        except ValueError:
            return False
            
            
            
            
            
            
    while True:
            
        print("操作する整理前のファイル群が入っているフォルダの絶対パスを入力してください-->", end="")
        path01 = input()
        
        if os.path.isdir(path01):
    
            files = os.listdir(path01)
            break
    
    
    while True:
        print("整理後のファイル群を格納するフォルダの場所のパスを入力してください-->", end="")
      
        path02 = input()
        if os.path.isdir(path02):
            print("整理後に使うフォルダを新たに作成しますか？(y/n)-->", end="")
            Ans = input()
      
            if Ans == "y":
                while True:
                      print("新たに作成するフォルダ名を入力-->", end="")
                      Name = input()
                      if isper(path02, Name):
                          if Name in os.listdir(path02):
                              print("そのフォルダはその場所に既に存在します")
                      
                          else:
                             flg = flg + 1
                             os.mkdir(os.path.join(path02, Name))
                             DIR01 = os.path.join(path02, Name)
                             break
                      else:
                          print("文字を入力してください")
                          continue
      
            elif Ans == "n":
                  print("使用する既存のフォルダ名を入力-->", end="")
                  Name = input()
                  if Name not in os.listdir(path02):
                      print("フォルダがありません")
                  else:
                      DIR01 = os.path.join(path02, Name)
                      break
            else:   
                print("yかnで答えてください")
                continue
            if flg == 1:
                break
            
    while True:
            flg = 0
            print("ファイル名から、格納するフォルダの中にファイル群を分けて格納するフォルダを作成します")
            files = os.listdir(path01)
            while True:
                    print("__[行]ファイル名　の一覧__")
                    for x in files:         
                        print(f'[{str(i)}]{x}')
                        i = i+1
                    i = 0
                    print("フォルダ名の基準となるファイルを行で指定してください(終了する場合は「end」と入力)-->", end="")
                    FL = input()
                    if FL == "end":
                        print("BYE")
                        time.sleep(3)
                        sys.exit()
                    if isint(FL):
                        FL = int(FL)
                        print(f'{files[FL]}で間違いないですか？(y/n)-->', end="")
                        Ans = input()
                        if Ans == "y":
                            break
                        else:
                            continue
                    else:
                        print("行は数値で指定してください")
                        continue
        
            while True:
                    print(f'{files[FL]}の区切り文字を指定してください(例 ： xxx_yyy_zzzなら区切り文字は"_")-->', end="")
                    SP = input()
                    if Valu(FL, SP):
                        print(f'{files[FL].split(SP)}で間違いないですか？(y/n)-->', end="")
                        Ans = input()
                        if Ans == "y":
                            break
                        else:
                            continue
                    else:
                        continue
            while True:
                    print(f'{files[FL].split(SP)}の内、ファイル名に使用する文字列の個数を入力してください(左から数える)-->', end="")
                    SL = input()
                    if isint(SL):
                        SL = int(SL)
                        print(f'{files[FL].split(SP)[:SL]}で間違いないですか？(y/n)-->', end="")
                        Ans = input()
                        if Ans == "y":
                            AR = files[FL].split(SP)[:SL]
                            break
                        else:
                            continue
                    else:
                        print("個数は数値で指定してください")
                        continue
                    
            while True:
                print(f'{files[FL].split(SP)[:SL]}を結合する文字を入力してください-->', end="")
                JI = input()
                print(f'作成するフォルダ名は{JI.join(files[FL].split(SP)[:SL])}でいいですか？(y/n)-->', end="")
                Ans = input()
                if Ans == "y":
                    DIR02 = JI.join(files[FL].split(SP)[:SL])
                    break
                else:
                    continue
                
            while True:
                if DIR02 not in os.listdir(DIR01):
                    os.mkdir(os.path.join(DIR01, DIR02))
                    break
                else:
                    print("そのフォルダは既に存在します、上書きしますか？(y/n)-->", end="")
                    Ans = input()
                    if Ans == "y":
                        break
                    elif Ans == "n":
                        while True:
                            print("上書きが拒否されました。プログラムを終了しますか？(y/n)-->", end="")
                            Ans = input()
                            if Ans =="y":
                                sys.exit()
                            elif Ans == "n":
                                flg = flg + 1
                                break
            if flg == 1:
                continue
            else:
                for file in files:
                    if AR == file.split(SP)[:SL]:
                        shutil.move(f'{path01}/{file}', f'{DIR01}/{DIR02}/{file}')
                print("処理が完了しました。同フォルダ内で処理を続けますか？(y/n)-->")
                Ans = input()
                if Ans == "y":
                    continue
                elif Ans == "n":
                    print("BYE")
                    time.sleep(3)
                    sys.exit()
                    
                

except IndexError:
    print("フォルダ内のファイルが無くなりました。プログラㇺを終了します")
    time.sleep(3)
    sys.exit()
    
    