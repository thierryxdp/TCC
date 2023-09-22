def uppCons(frase):
    """essa função recebe uma string e retorna todas as coansoantes maiúsculas;
    str->str"""
    c='bcdfghjklmnpqrstvwxyzç'
    x=''
    l=''
    cont=0
    while cont<len(frase):
        if frase[cont] in c:
            l=str.upper(frase[cont])
            x += l
        else:
            x += frase[cont]
        cont += 1
    return x