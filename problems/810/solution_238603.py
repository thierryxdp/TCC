def inverte(frase):
    '''Retorna a frase recebida na ordem inversa, sem letras
    maiúsculas e sem pontuação
 	string-> string'''
    n1 = str.lower(frase.replace('_',' ',))
    n2 = n1.replace(',',' ',)
    n3 = n2.replace(':',' ',)
    n4 = n3.replace('-',' ',)
    n5 = n4.replace('.',' ',)
    n6 = n5.split(' ')
    n7 = n6[::-1]
    n8 = str.join('',n7)
    return n8