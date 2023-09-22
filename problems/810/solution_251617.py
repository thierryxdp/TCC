def inverte(c):
    b=c.replace(".","").replace(",","").replace("!","").replace("?","").replace(":","").replace("-","").replace(";","")
    a=str.lower(b)
    c=a.split(' ')
    c.reverse()
    d=str(c)
    e=d.replace("'","").replace("[","").replace("]","").replace(",","")
    return e