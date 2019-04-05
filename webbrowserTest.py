#! python3
# webbrowserTest.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser,sys,pyperclip

if len(sys.argv) > 1:
    # get address from parameter
    address = " ".join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()

webbrowser.open("https://www.baidu.com/s?wd=" + address)