def inverte(frase):
    "Inverta uma frase sem maiusculas e pontuações; str->str"
    x=str.replace(frase,'.',' ')
    y=str.replace(x,',',' ')
    z=str.replace(y,'-',' ')
    w=str.replace(z,'!',' ')
    xx=str.replace(w,'?',' ')
    xy=xx.split()
    r=xy[::-1]
    return str.lower((str.join(r," ")))