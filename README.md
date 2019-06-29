# Simulate Keypress
This is a simulate keypress sample repo with few (personal) useful tools.
日本語版のREADME(説明書)は[こちら](README_JP.md)。

## Dependencies
Python 3.7.3
pipenv: stable 2018.11.26

## Installation
Make sure you have Python 3.7.3 and pipenv.
If you're on MacOS, install pyenv and pipenv with Homebrew
```shell:
$ brew install pyenv
$ pyenv install 3.7.3
$ brew install pipenv
```
Clone this repo.
```
$ git clone https://github.com/wisetlaloc/simulate_keypress
```
Change directory to project.
```
$ pyenv local 3.7.3
$ pipenv install
```

## Tools
### Hearstone pack opener
Hearthstone card opener (A program that presses space continuously).
#### Usage
Go to your hearthstone game, and to 'Open Packs'.
After Installation, at your terminal run `pipenv run start`.
Focus your hearthstone game window. Enjoy!
- Caution
  - The program stops automatically in 5 minutes. Run `pipenv run start` if you still have more packs to open.
  - The terminal will show you how many spaces are pressed.
  - type `Ctrl + C` on terminal if you want to stop the program(MacOS)
