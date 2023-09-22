def retirar_pontuação(frase):
    '''função que, dado uma frase, retorna a mesma sem as pontuações
    entrada:str
    saída:str'''
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    return frase
def inverte(frase):
    '''função que dada uma frase, ela é invertida 
    sem pontuação e com letras minusculas
    entrada = str,list
    saida = str'''
    frase = str.lower(frase)
    frase = retirar_pontuação(frase)
    frase = str.split(frase,' ')
    frase = str.join(' ',frase)
    frase = frase[len[frase]:0:-1]
    return frase