def inverte(frase):
    '''Retorna a frase recebida na ordem inversa, sem letras
    maiúsculas e sem pontuação
 	string-> string'''
    n1 = str.lower(frase.replace('_',' ',))
    n2 = n1.replace(',',' ',)
    n3 = n2.replace(':',' ',)
    n4 = n3.replace('-',' ',)
    n4 = n4[::-1]
    return n4 + ' '