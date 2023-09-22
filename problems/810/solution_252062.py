def inverte(string):
    x=str.lower(string)
    x=str.strip(x,",")
    z=str.strip(x,".")
    y=str.strip(z,"!")
    a=str.strip(y,"?")
    b=str.strip(a,"-")
    return b