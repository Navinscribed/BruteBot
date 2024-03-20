<p align="center">
<img src = "https://user-images.githubusercontent.com/51265978/89702444-f8a5f380-d95e-11ea-8210-79411e9fdd20.png"></img>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/language-python%203.x-blue">
  </a>
  <a href="https://webbot.readthedocs.io/">
    <img src="https://img.shields.io/badge/library-webbot-orange">
  </a>
  <a href="https://github.com/Navinscribed">
    <img src="https://img.shields.io/badge/author-Navinscribed-brightgreen">
 </a>
</p>

## BruteBot
- **BruteBot** is a Python-based tool that leverages the [webbot](https://webbot.readthedocs.io/) library to automate the process of brute-forcing login passwords, `particularly useful for login pages fortified with CSRF protection or random tokens`.

- The choice of webbot, a library derived from Selenium, was intentional. The goal was to emulate a user navigating the target website’s login page and attempting to brute-force the password in the most unobtrusive manner.

- This approach ensures that any random tokens that are generated when the login page gets loaded are automatically included in the subsequent login POST requests, thereby making the automation of password brute-forcing possible.

- Furthermore, it gives you a chance to visualize the browser's operations in real time, which can be useful for troubleshooting.
<br><br>
## How BruteBot Operates?
- It retrieves the login page via a GET request.

- It utilizes the username / email address and the password list provided by you.

- It submits these credentials to the server via multiple POST requests (each containing a unique username-password combination), alongside any additional random tokens if present  (such as: an anti-CSRF token, an arbitrary browser identifier, timestamp, etc.)

- It repeats this process until it successfully discovers the correct password.
<br><br>
## Requirements

1. Install `webbot` using the following command:

```bash
pip install webbot
```

2. Download or clone the repository.

3. Place your password list file in the same directory as BruteBot.py.
<br><br>
_That's it! You are good to go!_
<br><br>
## Usage

### Command
```
python BruteBot.py -t (LOGIN PAGE URL) -u USERNAME -p (PASSWORD LIST) --uid (USERNAME ELEMENT ID) --pid (PASSWORD ELEMENT ID) --bname (LOGIN BUTTON NAME) -m (visible / headless) -s (TIME IN SECONDS)
```

### Program Arguments
#### Required Arguments
- `-t` / `--target` : URL of the target website's login page

- `-u` / `--username` : A valid username / email address

- `-p` / `--plist` : Path of the password list file

- `--uid` : Username Element ID

- `--pid` : Password Element ID

- `--bname` : Name of the login button element

#### Optional Arguments
- `-m` / `--mode` : Sets the mode of operation

  - `headless` : To have all operations run in the background (Default mode: `headless`)

  - `visible` : To view the operations happening in your browser

- `-s` / `--time` : Duration, in seconds, for which the browser will wait before commencing the brute-forcing

- `-h` / `--help` : Shows the help message and exits
<br><br>
## Quickstart Guide

**Demo 1** - To run BruteBot with the default options:

```python
python BruteBot.py -t https://demo.testfire.net/login.jsp -u admin -p passwords.txt --uid uid --pid passw --bname Login
```

<img src="https://github.com/Navinscribed/media-repo/blob/master/BruteBot/BruteBot-Demo-1.gif"></img>

<br><br>

**Demo 2** - To see the browser tab(s) in action when BruteBot runs:

```python
python BruteBot.py -t https://demo.testfire.net/login.jsp -u admin -p passwords.txt --uid uid --pid passw --bname Login -m visible
```

<img src="https://github.com/Navinscribed/media-repo/blob/master/BruteBot/BruteBot-Demo-2.gif"></img>

<br><br>

**Demo 3** - To route the traffic through a network proxy while running BruteBot:

```python
python BruteBot.py -t https://demo.testfire.net/login.jsp -u admin -p passwords.txt --uid uid --pid passw --bname Login --proxy http://localhost:8080
```

<img src="https://github.com/Navinscribed/media-repo/blob/master/BruteBot/BruteBot-Demo-3.gif"></img>

<br>

## Disclaimer
- Please refrain from using this tool on websites without explicit permission, as doing so may be considered illegal or unethical.
- I bear no responsibility for any misuse of this tool.
<br><br>
## Acknowledgments
- This project utilizes the [webbot](https://webbot.readthedocs.io/) library, originally developed by the author [@nateshmbhat](https://github.com/nateshmbhat/).
- Special thanks to [@m-uma](https://github.com/m-uma/) for their invaluable offline contributions that were instrumental in the development of this tool.
<br><br>
## License & Contributions
- This project is licensed under the terms of the MIT license. Feel free to contribute, go ahead and submit a [Pull Request](https://github.com/Navinscribed/BruteBot/pulls).
- However, if you are considering making significant modifications, I would insist that you discuss with me first by opening an [Issue](https://github.com/Navinscribed/BruteBot/issues/new).
<br><br>
---
<span style="vertical-align: middle;">Like my work?</span>
<a href="https://www.buymeacoffee.com/navin.m" style="vertical-align: middle;">
  Buy me a coffee maybe?
  <img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" style="width: 30px; height: 30px; vertical-align: middle;">
</a>


