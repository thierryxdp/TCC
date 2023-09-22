def inverte(frase):
    frase_normal=str.split(sub(frase),' ')
    frase_invertida=frase_normal[-1:]
    invtxt=str.join(' ',frase_invertida)
    return invtxt.lower()