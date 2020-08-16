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
  <a href="https://github.com/navin-maverick">
    <img src="https://img.shields.io/badge/author-navin%20m-brightgreen">
 </a>
</p>

<h3 align="center">Password brute-forcing tool built upon Python 3.7 and <a href = "https://webbot.readthedocs.io/">webbot</a></h3>

---

+ **BruteBot** lets you brute-force login passwords. It is handy for login pages that have CSRF protection or any random tokens.

       Basically, the script
       1. GETs the login page,
       2. consumes the username / email and passwords fed by you, and
       3. POSTs those values to the server along with additional random parameters if any
          (could be an Anti-CSRF token or a browser window identifier or a time-stamp, etc.);
       4. loops the entire process until you get a hit, that is, the correct password.

+ I specifically used webbot (a library derived from Selenium) because I wanted to mimic the actions of a user browsing the target website login page and attempting to brute-force the password themselves, in the cleanest possible way.

+ That way, any additional random tokens that might get generated upon visiting the login page shall be automatically passed along in the subsequent login POST request, and the password brute-forcing automation can be accomplished.

+ Plus, it lets you see the browser in action. So, it becomes easier to visualize and helps while troubleshooting.

</br>

## Requirements:

1. Download and install the latest version of Python 3.x from [here](https://www.python.org/downloads/).
2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install 'webbot'.

```bash
pip3 install webbot
```

3. Download Brutebot.py to your local directory.
4. Place your password list file in the same directory as BruteBot.py.

</br>

That's it! You are good to go!

</br>

## Usage:

```
python3 BruteBot.py -t (LOGIN PAGE URL) -u USERNAME -p (PASSWORD LIST) --uid (USERNAME ELEMENT ID) --pid (PASSWORD ELEMENT ID) --bname (LOGIN BUTTON NAME) -m (visible / headless) -s (TIME IN SECONDS)
```

</br>

Here, this might "help":

<img width="1440" alt="BruteBot-Help" src="https://user-images.githubusercontent.com/51265978/89457710-6d243b00-d783-11ea-8b86-17cb29f5259a.png">

</br>

## Quickstart guide:

**Demo 1** - To run BruteBot with default options:

```python
python3 BruteBot.py -t https://demo.testfire.net/login.jsp -u admin -p passwords.txt --uid uid --pid passw --bname Login
```

<img src="https://github.com/navin-maverick/media-repo/blob/master/BruteBot/BruteBot-Demo-1.gif"></img>

</br></br>

**Demo 2** - To see the browser(s) in action when BruteBot runs:

```python
python3 BruteBot.py -t https://demo.testfire.net/login.jsp -u admin -p passwords.txt --uid uid --pid passw --bname Login -m visible
```

<img src="https://github.com/navin-maverick/media-repo/blob/master/BruteBot/BruteBot-Demo-2.gif"></img>

</br></br>

**Demo 3** - To route the traffic through a proxy while running BruteBot:

```python
python3 BruteBot.py -t https://demo.testfire.net/login.jsp -u admin -p passwords.txt --uid uid --pid passw --bname Login --proxy http://localhost:8080
```

<img src="https://github.com/navin-maverick/media-repo/blob/master/BruteBot/BruteBot-Demo-3.gif"></img>

</br>

---

**Like my work?** <a href="https://www.buymeacoffee.com/navin.m">Buy me a coffee maybe?</br></br><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg"></img></a>
