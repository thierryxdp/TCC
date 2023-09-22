def inverte(frase):
    '''Função que retorna uma frase na oredem inversa
       string->string'''
    listaPalavras=str.split(frase, ' ')
    list.reverse(listaPalavras)
    fraseInv=str.join(' ',listaPalavras)
    return fraseInv