def inverte (texto):
    '''função em que dada uma frase retorne outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa,sem letras maiúsculas e sem pontuação;
    str -> str'''
    F1=(retira_pontuacao(texto))
    F2=str.lower(F1)
    lista=str.split(F2)
    lista.reverse()
    return str.join(' ',lista)