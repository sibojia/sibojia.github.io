import pyperclip, platform
s = pyperclip.paste()
l = [i.strip() + '\\n\\' for i in s.split('\n')]
nl = '\n'
if platform.system() == 'Windows':
	nl = '\r\n'
pyperclip.copy(nl.join(l))