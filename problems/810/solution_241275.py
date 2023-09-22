def inverte(frase):
    '''retorna uma frase diferente da inicial, que contem as mesmas palavras da frase de entrada na ordem inversa; string->str'''
    filtro= frase.replace(';',' ')
    filtro2= filtro.replace('-',' ')
    filtro3= filtro2.replace('!',' ')
    filtro4= filtro3.replace('?',' ')
    filtro5= filtro4.replace('.',' ')
    filtro6= filtro5.replace(':',' ')
    filtro7= filtro6.replace(',',' ')
    separador= filtro7.split()
    lista= separador[::-1]
    funcao= ' '.join(lista)
    return funcao.lower()