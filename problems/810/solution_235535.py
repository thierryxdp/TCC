def inverte(frase):
    '''recebe uma frase,transforma em uma lista e retira todas as pontuações, depois disso inverte a ordem 
    e junta ela,trazendo o inverso da frase
    str->list->str'''
    frase=frase.replace('.',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('?',' ')
    frase=frase.split()
    frase=list(frase)
    frase=frase[::-1]
    frase=str.join(' ',frase)
    nova_frase=str(frase)
    return nova_frase.lower()