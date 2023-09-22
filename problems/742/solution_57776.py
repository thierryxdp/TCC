def substitui(s,x,i):
    '''retorna uma string s, com o caractere x  na posição i:
    str, str, int --> str'''
    texto = str(s)
    print(texto.replace('texto[i]','x'))
    return