def inverte (frase):
    '''função em que dada uma frase retorne outra frase que contenha as mesmas
    palavras da frase de entrada na ordem inversa,sem letras maiúsculas e sem
    pontuação;
    str -> str'''
    f1=(retira_pontuacao(frase))
    f2=str.lower(f1)
    lista=str.split(f2)
    lista.reverse()
    return str.join(' ',lista)