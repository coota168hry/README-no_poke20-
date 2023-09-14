#=========
README
#=========
#ポケモンのリスト、出力ファイル名を入力して実行してください
#本来であれば入力ファイル等作成するべきですが、初期データ用意時のみの利用のため整備していません。
#仮想環境（venv）で実行しました

#=========
#00.準備
#=========
#ライブラリインポート
from bs4 import BeautifulSoup
from string import Template
import requests
#import re


poke_names = [
#凡例：
#'フシギダネ',
#'フシギソウ', ...
#以下に取得したいポケモンの名称を入力

]

#出力するファイル名を入力
file_name = 'example_1.csv'

#=========
#01.実行
#=========
for poke_name in poke_names:
  res = requests.get('https://wiki.ポケモン.com/wiki/{}'.format(poke_name))
  soup = BeautifulSoup(res.text,'html.parser')
  tags = soup.find('div',id='mw-content-text')
  tagsdl = tags.find('dl')

  tagsdt = tagsdl.find_all('dt')
  #ループで一つずつfind
  f = open(file_name, 'a')
  for x in tagsdt:
    #a = x.find('a')  成功したけど、「、」以降が取れていない
    #a = x.contents 失敗
    #a = x.descendants 失敗
    if '、' in x:
      a = x.find_all('a')
      for x2 in a:  #この時点では['赤・緑', 'ファイアレッド', 'ソード']の状態で入ってる
        for x3 in x2:
          #print(poke_name + ',' + str(x3) + ',' + x.next_sibling.next_sibling.string)
          f.write(poke_name + ',' + str(x3) + ',' + x.next_sibling.next_sibling.string + '\n')
        #print(x.next_sibling.next_sibling.string)
    else:
      #print(poke_name + ',' + str(x.string) + ',' + x.next_sibling.next_sibling.string)
      f.write(poke_name + ',' + str(x.string) + ',' + x.next_sibling.next_sibling.string + '\n')
  f.close()
