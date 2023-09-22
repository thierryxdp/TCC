def inverte (frase):
    '''funcao que inverte frase e tira a letra maiuscula'''
    lista = frase
    a = (lista[::-1])
    a = str.lower(frase)
    a = str.replace(frase,'?',' ')
    a = str.replace(a,'-',' ')
    a = str.replace(a,',',' ')
    a = str.replace(a,'.',' ')
    a = str.replace(a,'!',' ')
    return a