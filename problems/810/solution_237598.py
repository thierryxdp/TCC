def inverte(frase):
    frase_inverte= str.replace(frase,'-',' ')
    frase_inverte= frase_inverte.replace(',',' ')
    frase_inverte= frase_inverte.replace('.',' ')
    frase_inverte= frase_inverte.replace('!',' ')
    frase_inverte= frase_inverte.replace('?',' ')
    frase_inverte= frase_inverte[::-1]
    frase_inverte= str.split(frase_inverte)
    frase_inverte= str.join(' ',(frase_inverte))
    frase_inverte= str.lower(frase_inverte)
    return frase_inverte