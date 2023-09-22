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
    lista = i[:]
    return lista[0:4]