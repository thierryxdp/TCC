def inverte(frase):
    '''funcao que dada uma frase retorna uma outra frase que contenha as mesmas palavras de entrada na ordem inversa
    str->str'''
    minusc=str.lower(frase)
    rempont=rempontuacao(minusc)
    lista_frase=str.split(remport)
    lista_invertida=lista_frase[::-1]
    return lista_invertida