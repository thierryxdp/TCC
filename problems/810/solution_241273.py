def inverte(frase):
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