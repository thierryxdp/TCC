def uppCons(frase):
    """essa função recebe uma frase como entrada e retorna
    a mesma frase, porém com todas as suas consoantes em maiúsculas;
    str->str"""
    c = 'bcdfghjklmpnpqrstvwxyz'
    x = ''
    l = ''
    cont = 0
    while cont < len(frase):
        if frase[cont] in c:
            l = str.upper(frase[cont])
            x += 1
        else:
            x += frase[cont]
        cont += 1
    return x