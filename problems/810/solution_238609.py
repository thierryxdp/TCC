def inverte(frase):
    '''Retorna a frase recebida na ordem inversa, sem letras
    maiúsculas e sem pontuação
 	string-> string'''
    n1 = str.lower(frase.replace('_',' ',))
    n2 = n1.replace(',',' ',)
    n3 = n2.replace(':',' ',)
    n4 = n3.replace('-',' ',)
    n5 = n4.replace('.',' ',)
    n6 = n5.replace('!',' ',)
    n7 = n6.replace('...',' ',)
    n8 = n7.replace('?',' ',)
    n9 = n8.split(' ')
    n10 = n9[::-1]
    n11 = str.join(' ',n10)
    n12 = n11.lstrip(' ')
    return n12