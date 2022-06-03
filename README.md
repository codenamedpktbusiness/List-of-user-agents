# List and Update of User-Agents
List and update of major web + mobile browser user agent strings today. +1 Bonus script to scrape :) 

Requirements:
Python 3.10 minimum
Android 10 with Termux Mobile App installed
Ubuntu 20.04 minimum, or equivalent Linux for Linux Desktop
Windows 10 with Python for Windows 3.10 installed at least and added to PATH variable when installing.

For above mentioned operating systems and Apps hardware requirements, copy the keywords and Google them.
usage:
<br>If user having Termux App, clone this repo and run:</br>
<br>`./user-agent-termux.py` </br>
When running with Termux App, no rooting required on Android.

<br>For Desktop users, clone this repo and run:</br>
<br>`./user-agent-linux.py`</br>

User do not need to use sudo (prompt yes if you are on Windows with Admin) for root (Admin on Windows) privileges. 

We also have GitHub Workflow automation if you fork this repo with thanks!

Note to Windows Users:

After installing Python for Windows, please do following before running this App:

```cmd 
python -m ensurepip --upgrade
pip install --upgrade --no-cache-dir -qqq pip setuptools toml wheels upgrade_ensurepip 
python -m ensurepip --upgrade --default-pip
pip install --upgrade --no-cache-dir -qqq requests bs4
```

Please report bugs on issues tab.
