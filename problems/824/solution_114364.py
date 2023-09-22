def uppCons(frase):
    """retorna a frase com todas as consoantes em maiúsculas e os demais caracteres mantidos.
    str->str"""
    indice=0
    while indice<len(frase):
        if frase[indice] not in 'AEIOUaeiou':
            str.upper(frase[indice])
        indice=indice+1
    return frase