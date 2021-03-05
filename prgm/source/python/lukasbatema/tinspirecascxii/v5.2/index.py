# Tag input.
tagInfo=''

# <html>...</html> element.
openHtml='<html>'
closedHtml='</html>'
def htmlOpen():
  print('<!DOCTYPE html>')
  print('  ' + openHtml)
  return

def htmlClosed():
  print('  ' + closedHtml)
  return

# <html>...</html> element.
openHead='<head>'
closedHead='</head>'
def headOpen():
  print('  ' + openHead)
  return

def headClosed():
  print('  ' + closedHead)
  return

# <title>...</title> element.
openTitle='<title>'
closedTitle='</title>'
def title():
  print('    ' + openTitle + input(tagInfo) + closedTitle)
  return

# <link...> element.
openLink='<link '
def link():
  print('    ' + openLink + '>')
  return

# <body>...</body> element.
openBody='<body>'
closedBody='</body>'
def bodyOpen():
  print('    ' + openBody)
  return

def bodyClosed():
  print('    ' + closedBody)
  return

# <footer>...</footer> element.
openHtml='<footer>'
closedHtml='</footer>'
def footerOpen():
  print('  ' + openFooter)
  return

def footerClosed():
  print('  ' + closedFooter)
  return

# <h1>...</h1> element.
openH1='<h1>'
closedH1='</h1>'
def h1():
  print('      ' + openH1 + input(tagInfo) + closedH1)
  return

# <h2>...</h2> element.
openH2='<h2>'
closedH2='</h2>'
def h2():
  print('      ' + openH2 + input(tagInfo) + closedH2)
  return

# <h3>...</h3> element.
openH3='<h3>'
closedH3='</h3>'
def h3():
  print('      ' + openH3 + input(tagInfo) + closedH3)
  return

# <h4>...</h4> element.
openH4='<h4>'
closedH4='</h4>'
def h4():
  print('      ' + openH4 + input(tagInfo) + closedH4)
  return

# <h5>...</h5> element.
openH5='<h5>'
closedH5='</h5>'
def h5():
  print('      ' + openH5 + input(tagInfo) + closedH5)
  return

# <h6>...</h6> element.
openH6='<h6>'
closedH6='</h6>'
def h6():
  print('      ' + openH6 + input(tagInfo) + closedH6)
  return

# <p>...</p> element.
openP='<p>'
closedP='</p>'
def pOpen():
  print('      ' + openP)
  return

def pClosed():
  print('      ' + closedP)
  return

# <b>...</b> element.
openB='<b>'
closedB='</b>'
def b():
  print('        ' + openB + input(tagInfo) + closedB)
  return

# <i>...</i> element.
openI='<i>'
closedI='</i>'
def i():
  print('        ' + openI + input(tagInfo) + closedI)
  return

# <u>...</u> element.
openU='<u>'
closedU='</u>'
def u():
  print('        ' + openU + input(tagInfo) + closedU)
  return

# <pre>...</pre> element.
openPre='<pre>'
closedPre='</pre>'
def pre():
  print('        ' + openPre + input(tagInfo) + closedPre)
  return

# <strong>...</strong> element.
openStrong='<strong>'
closedStrong='</strong>'
def strong():
  print('        ' + openStrong + input(tagInfo) + closedStrong)
  return

# <em>...</em> element.
openEm='<em>'
closedEm='</em>'
def em():
  print('        ' + openEm + input(tagInfo) + closedEm)
  return

# <sub>...</sub> element.
openSub='<sub>'
closedSub='</sub>'
def sub():
  print('        ' + openSub + input(tagInfo) + closedSub)
  return

# <sup>...</sup> element.
openSup='<sup>'
closedSup='</sup>'
def sup():
  print('        ' + openSup + input(tagInfo) + closedSup)
  return

# <del>...</del> element.
openDel='<del>'
closedDel='</del>'
def delete():
  print('        ' + openDel + input(tagInfo) + closedDel)
  return

# <s>...</s> element.
# Same as <del>...</del> element.
openS='<s>'
closedS='</s>'
def s():
  print('        ' + openS + input(tagInfo) + closedS)
  return

# <ins>...</ins> element.
openIns='<ins>'
closedIns='</ins>'
def ins():
  print('        ' + openIns + input(tagInfo) + closedIns)
  return

# <br> element.
openBr='<br>'
def br():
  print(openBr)
  return

# <address>...</address> element.
openAddress='<address>'
closedAddress='</address>'
def addressOpen():
  print('        ' + openAddress)
  return

def addressClosed():
  print('        ' + closedAddress)
  return

# Instructions
def pytmlHelp(tagInfo):
  if tagInfo=='html':
    print('Usage: htmlOpen() for open html tag and htmlClosed() for closed html tag. Type, "htmlOpen" for more details on the open tag and type, "htmlOpen" for more details on the closed tag.')
    print('')
    print('Displays:')
    print('<!DOCTYPE html>')
    print('  ' + openHtml)
    print('*user input*')
    print('  ' + closedHtml)
    return
  elif tagInfo=='htmlOpen()' or 'htmlOpen':
    print('Usage: htmlOpen() for the open html tag.')
    print('')
    print('Displays:')
    print('<!DOCTYPE html>')
    print('  ' + openHtml)
    print('*user input*')
    return
  elif tagInfo=='htmlClosed()' or 'htmlClosed':
    print('Usage: htmlClosed() for closed html tag.')
    print('')
    print('Displays:')
    print('  ' + closedHtml)
    return
  elif tagInfo=='head':
    print('Usage: headOpen() for the open head tag and headClosed() for the closed head tag. Type, "headOpen" for more details on the open tag and type, "headClosed" for more details on the closed tag.')
    print('')
    print('Displays:')
    print('    ' + openHead)
    print('*user input*')
    print('    ' + closedHead)
    return
  elif tagInfo=='headOpen()' or 'headOpen':
    print('Usage: headOpen() for the open head tag.')
    print('')
    print('Displays:')
    print('    ' + openHead)
    print('*user input*')
    return
  elif tagInfo=='headClosed()' or 'headClosed':
    print('Usage: headClosed() for closed head tag.')
    print('')
    print('Displays:')
    print('    ' + closedHead)
    return
  elif tagInfo=='title()' or 'title':
    print('Usage: title()')
    print('')
    print('Displays:')
    print('      ' + openTitle + '*user input*' + closedTitle)
    return
  elif tagInfo=='link()' or 'link':
    print('Usage: link()')
    print('')
    print('Displays:')
    print('      ' + openLink + '*user input*' + '>')
    return
  elif tagInfo=='body':
    print('Usage: bodyOpen() for open tag and bodyClosed() for closed tag. Type, "bodyOpen()" for more details on the open tag and type, "bodyClosed()" for more details on the closed tag.')
    print('')
    print('Displays:')
    print('    ' + openBody)
    print('*user input*')
    print('    ' + closedBody)
    return
  elif tagInfo=='bodyOpen()' or 'bodyOpen':
    print('Usage: bodyOpen() for open body tag')
    print('')
    print('Displays:')
    print('    ' + openBody)
    print('*user inuput*')
    return
  elif tagInfo=='bodyClosed()' or 'bodyClosed':
    print('Usage: bodyClosed() for closed body tag.')
    print('')
    print('Displays:')
    print('    ' + closedBody)
    return
  elif tagInfo=='footer':
    print('Usage: footerOpen() for open tag and footerClosed() for closed tag. Type, "footerOpen()" for more details on the open tag and type, "footerClosed()" for more details on the closed tag.')
    print('')
    print('Displays:')
    print('    ' + openFooter)
    print('*user input*')
    print('    ' + closedFooter)
    return
  elif tagInfo=='footerOpen()' or 'footerOpen':
    print('Usage: footerOpen() for open footer tag.')
    print('')
    print('Displays:')
    print('    ' + openFooter)
    print('*user input*')
    return
  elif tagInfo=='footerClosed()' or 'footerClosed':
    print('Usage: footerClosed() for closed footer tag.')
    print('')
    print('Displays:')
    print('    ' + closedFooter)
    return
  elif tagInfo=='h1()' or 'h1':
    print('Usage: h1()')
    print('')
    print('Displays:')
    print('      ' + openH1 + '*user input*' + closedH1)
    return
