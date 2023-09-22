def inverte(frase):
    '''função que dade uma frase retorne uma outra frase que 
    contenha as mesmas palavras da frase de entrada na ordem 
    inversa,sem letras maiúsculas, e sem ppontuação;
    string->string'''
    s=str.lower(retira_pontuacao(frase))
    x=str.split(s)
    y=x[::-1]
    z=str.join(' ',y)
    return z