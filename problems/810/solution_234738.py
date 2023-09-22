def inverte(frase):
    '''Função que dada uma frase, retorne uma outra que possui as mesmas palavras da frase de entrada, mas na ordem inversa;str -> str'''
    frase1 = str.replace(frase,'-',' ')
    frase2 = str.replace(frase1,',',' ') 
    frase3 = str.replace(frase2,':',' ') 
    frase4 = str.replace(frase3,';',' ')
    frase5 = str.replace(frase4,'?', ' ')
    frase6 = str.replace(frase5,'.',' ')
    frase7 = str.replace(frase6,'!',' ')
    listapalavras = str.split(frase7,)
    fatiamentolista = listapalavras[len(listapalavras)::-1]
    return str.lower(str.join(' ',fatiamentolista)),' '