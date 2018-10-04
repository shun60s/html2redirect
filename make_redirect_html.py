# -*- coding: UTF-8 -*-
#--------------------------------------------------------------------------
#（内容）
# カレントディレクトリ以下の
# 既在のhtmlファイルと同じ名称をもつ、リダイレクトの内容のhtml(UTF-8)を生成する。
#
# (以下を設定する）
# 移転先のURL
url_org='http://example.jp/'
# リダイレクト内容のhtmlの出力ディレクトリー
dir_out='.\\output_html\\'
# メッセージ文
mess0='本サイトは移転しました。5秒後にジャンプします。'
# ファイル拡張子
ext0='.html'


# Check version 
# python 3.6.4 win32 (64bit) 
# windows 10 (64bit) 

import os
import glob   # サブディレクトリの探索に再帰的な glob を使っているため、python 3.5以上が必要
import codecs

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
    
    # html文を書きだす
    with codecs.open(path0, 'w','utf-8') as f:
        f.write( '<!DOCTYPE html>\n' )
        f.write( '<html lang="ja">\n' )
        f.write( '<head>\n')
        f.write( '<meta charset="utf-8">\n' )
        f.write( '<rel="canonical" href="' )
        f.write( url0 )
        f.write( '">\n')
        f.write( '<meta http-equiv="refresh" content="5;URL=' )
        f.write( url0 )
        f.write( '">\n' )
        f.write( '<title>リダイレクト</title>\n')
        f.write( '</head>\n')
        f.write( '<body>\n')
        f.write( '<h1>リダイレクト</h1>\n')
        f.write( '<p>' )
        f.write( mess0 )
        f.write( '</p><br>\n' )
        f.write( '<p>ジャンプしない場合は、以下のURLをクリックしてください。</p>\n')
        f.write( '<p><a href="')
        f.write( url0 )
        f.write( '">移転先のページ</a></p>\n' )
        f.write( '</body>\n')
        f.write( '</html>\n')

print ('finished')
