# リダイレクトhtmlの自動生成

## 概要  
ホームページの引っ越しのために作成した。  
カレントディレクトリ以下の既在のhtmlファイルと同じ名称をもつリダイレクト用のhtmlや、
既在のhtmlファイルにcanonicalタグを追加したhtmlを生成するもの。


## 内容  

カレントディレクトリ以下の既在のhtmlファイルと同じ名称をもつ、リダイレクトの内容のhtml(UTF-8)を生成する。  
移転先のURLや保存先などを設定する。  
```
python3 make_redirect_html.py
```

カレントディレクトリ以下の既在のhtmlファイルの<head>の次にcanonicalタグを追加したhtmlファイルを生成する。  
移転先のURLや保存先などを設定する。  

```
python3 add_canonical_html.py
```

カレントディレクトリ以下の既在のhtmlファイルの<body>の次にメッセージ文を追加したhtmlファイルを生成する。  
移転先のURLや保存先やメッセージなどを設定する。  
```
python3 add_message_html.py
```

## 使用上の注意  
移動元と移動先のディレクトリー構造とファイル名は同じものであると仮定している。 
<head>や<body>の続きタグやメッセージを追加するだけで、改行コードは追加していない。　
<head> ～</head>の間にutf-8又はUTF-8 の記述がある場合、utf-8として追加する（不完全な）仕様になっている。  
サブディレクトリの探索に再帰的な glob を使っているため、python 3.5以上が必要。  
Windowsで動作を確認している。他のOSやpython 2では文字コードの扱いが異なるため、ソースの修正が必要。  
sampleフォルダーの中に、元のhtmlと生成したhtmlのサンプルがあります。  

## 免責事項  
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS 
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  
#### 上記はMITライセンスからの抜粋です。