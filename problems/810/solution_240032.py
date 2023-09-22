def inverte(txt):
    a = ['!','?','.',',',':',';','-']
    txt = txt.replace(a[0],' ')
    txt = txt.replace(a[1],' ')
    txt = txt.replace(a[2],' ')
    txt = txt.replace(a[3],' ')
    txt = txt.replace(a[4],' ')
    txt = txt.replace(a[5],' ')
    txt = txt.replace(a[6],' ')
    txt = txt.lower()
  	txtx = txt.split()
    txtx = txtx.reverse()
    txt = str.join(" ",txt)
    return txt