
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
