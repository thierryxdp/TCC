def inverte(frase):
    '''Função que retorna o inverso de uma frase dada
    frase=str->str'''
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase,'.',' ')
    texto = str.split(frase)
    inve = texto[::-1]
    inve1 = str.join(' ',inve)
    inve2 = str.lower(inve1)
    return inve2