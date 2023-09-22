def inverte(frase):
    s = frase.replace('.',' ').replace(',',' ').replace('!',' ').replace('-',' ').replace('?',' ').replace(';',' ').replace(':',' ').replace('...',' ')
    minusculo = str.lower(frase)
    frase_dividida = str.split(minusculo)
    tamanho = len(frase_dividida)
    frase_invertida = frase_dividida[tamanho::-1]
    frase_final = frase_invertida.replace('.','').replace(',','').replace('!','').replace('-','').replace('?','').replace(';','').replace(':','').replace('[','').replace(']','')
    return frase_invertida