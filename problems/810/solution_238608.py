def inverte(frase):
    '''Retorna a frase recebida na ordem inversa, sem letras
    maiúsculas e sem pontuação
 	string-> string'''
    n1 = str.lower(frase.replace('_',' ',))
    n2 = n1.replace(',',' ',)
    n3 = n2.replace(':',' ',)
    n4 = n3.replace('-',' ',)
    n5 = n4.replace('.',' ',)
    n6 = n4.replace('!',' ',)
    n7 = n4.replace('...',' ',)
    n8 = n4.replace('?',' ',)
    n9 = n5.split(' ')
    n10 = n6[::-1]
    n11 = str.join(' ',n7)
    n12 = n8.lstrip(' ')
    return n12