# -*- coding: UTF-8 -*-
#--------------------------------------------------------------------------
#（内容）
# カレントディレクトリ以下の
# 既在のhtmlファイルの<body>の次にメッセージ文を追加したhtmlファイルを生成する。
#
# (以下を設定する）
# 移転先のURL
url_org='http://example.jp/'
# <body>の次にメッセージ文を追加したhtmlの出力ディレクトリー
dir_out='.\\output_html\\'
# ファイル拡張子
ext0='.html'
# メッセージ文= mess0 + url0 + mess1
mess0='<font color="red"><b>当ページは<a href=”'
mess1='”>ここに</a>に移転しました。</b></font><br><br>'

# Check version 
# python 3.6.4 win32 (64bit) 
# windows 10 (64bit) 

import os
import glob   # サブディレクトリの探索に再帰的な glob を使っているため、python 3.5以上が必要
import codecs

def comp0( a, b):
    # aの中のbの位置を返す。見つからない場合は -1を返す。
    b=b.encode('utf-8')
    if len(a) < len(b):
        return -1
    else:
        for i in range( len(a)-len(b)):
            code=i
            for j in range( len(b)):
                if a[j+i] != b[j]:
                    code=-1
                    break
            if code >-1:
                break
        if code != -1 :
            code += len(b)
        return code

# カレントディレクトリ以下のファイルの中でファイル拡張子が htmlのリストを作成する
List0=glob.glob(".\**",recursive=True)
List1=[s for s in List0 if s.endswith( ext0 ) and not s.startswith(dir_out) ]
print ('number of files ', len(List1))
print ('output directory ', dir_out)

for path_org in List1:
    # set output directory
    path0 = path_org.replace('.\\',dir_out)
    # create target URL address
    url0= url_org  + (path_org.replace('.\\','')).replace('\\','/')
    # create new directory as output
    if not os.path.exists(os.path.dirname(path0).replace('.\\','')):
        os.makedirs( os.path.dirname(path0).replace('.\\',''))
    # show original file path
    print (path_org)
    fin= open(path_org, 'rb')
    data_org=fin.read()
    fin.close()
    # check tag position
    c0=comp0(data_org, '<head>' )      # <head> タグの位置を返す。見つからない場合は -1を返す。
    c1=comp0(data_org, '</head>' )     # </head> タグの位置を返す。見つからない場合は -1を返す。
    c2a=comp0(data_org[c0:c1], 'utf-8') # c0とc1の間に　utf-8 の位置を返す。見つからない場合は -1を返す。
    c2b=comp0(data_org[c0:c1], 'UTF-8') # c0とc1の間に　UTF-8 の位置を返す。見つからない場合は -1を返す。
    c3=comp0(data_org, '<body>' )       # <body> タグの位置を返す。見つからない場合は -1を返す。

    
    if c3 > 0 :    #  <body>　タグの位置が既知の場合は <head>の次に以下を追加する。
        if c2a > -1 or c2b > -1:
            # <head> ～</head>の間にutf-8又はUTF-8 の記述がある場合。この判別方法は不完全である。
            all0 = data_org[0:c3] + mess0.encode('utf-8') + url0.encode('utf-8') + mess1.encode('utf-8') + data_org[c3:]
        else:
            #  Windows 環境のデフォルト文字コード shift-JIS
            all0 = data_org[0:c3] + mess0.encode('shift-jis') + url0.encode('shift-jis') + mess1.encode('shift-jis') + data_org[c3:]
        #　上書きしてしまうので注意！
        fout= open(path0, 'wb')
        fout.write( all0 )
        fout.close()
    else:
        print ('ERROR: cannot find <body> tag. No proceed')

print ('finished')
