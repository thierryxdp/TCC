def inverte(string):
    x=str.lower(string)
    c=str.strip(x,",")
    z=str.strip(c,".")
    y=str.strip(z,"!")
    a=str.strip(y,"?")
    b=str.strip(a,"-")
    return b