# Simulate Keypress
Pythonでのマウス／キーボード操作のサンプルレポジトリです。
英語版のREADME(説明書)は[こちら](README.md)。

## ツールのバージョン等
Python 3.7.3
pipenv: stable 2018.11.26

## インストール方法
Python 3.7.3 and pipenvが必要です。
MacOS なら下記のようにHomebrewでpyenvとpipenvをインストールしましょう。
```shell:
$ brew install pyenv
$ pyenv install 3.7.3
$ brew install pipenv
```
このレポジトリをcloneします。
```
$ git clone https://github.com/wisetlaloc/simulate_keypress
```
このプロジェクトのルートに移動して、
```
$ pyenv local 3.7.3
$ pipenv install
```
以上で完了です。

## ツール
### ハースストーンのパック開封自動化
ハースストーンのパックの開封を自動化します。(つまり、スペースキーを押し続けるプログラムです。)
#### 使用方法
ハースストーン(PC版)のパック開封画面へ行き、ターミナルにて`pipenv run start`を実行してください。
実行後すぐにハースストーンのゲーム画面にフォーカスを当ててください。
- 注意
  - プログラムは約5分で停止します。まだパックがある場合は再度`pipenv run start`してください。
  - ターミナルには押されたスペースキーの個数が表示されます。
  - 途中終了したい場合は`Ctrl + C`で停止します。(MacOSの場合)
