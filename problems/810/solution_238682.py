def inverte(frase):
    """ Essa função recebe uma frase e retorna a mesma na ordem inversa
    sem pontuação e nem letras maiúsculas. str-> str"""
    x = str.replace(frase,".",' ')
    y = str.replace(x,",",' ')
    z = str.replace(y,":",' ')
    h = str.replace(z,";",' ')
    d = str.replace(h,"-",' ')
    e = str.replace(d,"!",' ')
    i = str.replace(e,"?",' ')
    t = str.lower(i)
    lista = t[:]
    lista1 = str.split(lista[::-1],' ')
    lista2 = str.join(' ',lista1[::-1])
    return lista2