def inverte(f):
    '''
    Função que dada uma frase retorna uma outra frase contendo as mesmas palavras na
    ordem inversa, sem letras maiúsculas, e sem pontuação.
    str-> lista
    '''
def inverte(frase):
    '''
    
    '''
    um = str.replace(frase,'-',' ')
    dois = str.replace(um,',',' ') 
    tres = str.replace(dois,':',' ')
    quatro = str.replace(tres,';',' ')
    cinco = str.replace(quatro,'.',' ')
    seis = str.replace(cinco,'?',' ')
    sete = str.replace(seis,'!',' ')
    
    final = str.lower(sete)
    lista = str.split(final)
    invertida = list(reversed(lista))
    lista_final = ' '.join(invertida)
    return lista_final