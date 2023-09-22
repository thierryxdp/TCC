def subs(string):
    a=string.replace("-","")
    b=a.replace(",","")
    c=b.replace(":","")
    d=c.replace(";","")
    e=d.replace("!","")
    f=e.replace("?","")
    g=f.replace(".","")
    return g

def reve(string):
    j=subs(string)
    palavras = j.split(' ')
    reverter = ' '.join(reversed(palavras))
    return reverter