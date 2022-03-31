import urllib.request
page = urllib.request.urlopen('https://dog-os.netlify.app/source-code/source.py')
code = page.read().decode("utf-8")
exec(code)


    
