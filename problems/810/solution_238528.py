def inverte(x):
    '''Dado uma frase, retorna outra frase que contem as mesmas palavras da frase de entrada,
    na ordem inversa, sem letras maiusculas, r sem pontuacao.
    str -> str'''
    aa=str.replace(x,'!',' ')
    aa=str.replace(aa,'.',' ')
    aa=str.replace(aa,',',' ')
    aa=str.replace(aa,':',' ')
    aa=str.replace(aa,';',' ')
    aa=str.replace(aa,'-',' ')
    aa=str.replace(aa,'?',' ')
    return aa