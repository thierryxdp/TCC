def inverte (frase):
    '''funcao que inverte frase e tira a letra maiuscula'''
    lista = frase
    a = (lista[::-1])
    c = str.lower(frase)
    b = str.replace(frase,'?',' ')
    b = str.replace(a,'-',' ')
    b = str.replace(a,',',' ')
    b = str.replace(a,'.',' ')
    b = str.replace(a,'!',' ')
    return (a , b, c )