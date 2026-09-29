# Wraps index.html (artifact form, no doctype) into a full page for GitHub Pages.
import sys
src,dst=sys.argv[1],sys.argv[2]
s=open(src).read()
head='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="manifest" href="manifest.json">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="description" content="A playable walkthrough of Stephen King's The Gunslinger (1982 text). Non-commercial fan project.">
'''
i=s.index('</style>')+len('</style>')
open(dst,'w').write(head+s[:i]+'\n</head>\n<body>\n'+s[i:]+'\n</body>\n</html>\n')
