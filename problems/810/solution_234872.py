def inverte(frase):
    '''função que retorna outra frase contendo as mesmas palavras da frase de entrada na ordem inversa
    str->str'''
    frase = retira_pontuacao(frase)
    frase = str.split(frase,-1::-1)
    frase = str.join(' ',frase)
    return str.lower