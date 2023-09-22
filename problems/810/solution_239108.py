def inverte(s):
    '''Função que inverte dada uma frase;str->str'''
    listaPalavras=str.split(removePontuacao(s),' ')
    StringInvertida=str.join(' ',listaPalavras[::-1])
    return StringInvertida