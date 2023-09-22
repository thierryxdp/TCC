def inverte(frase):
    s = frase.replace('.',' ').replace(',',' ').replace('!',' ').replace('-',' ').replace('?',' ').replace(';',' ').replace(':',' ').replace('...',' ')
    tamanho = len(s)
    frase_invertida = s[tamanho::-1]
    return frase_invertida