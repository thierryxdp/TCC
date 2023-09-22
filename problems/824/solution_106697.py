def uppCons(frase):
    """A função recebe uma frase e retorna a mesma frase com todas as consoantes em maiúsculo;
    str->str"""
    indice=1
    frase=str.upper(frase)
    while indice<len(frase):
        if frase[indice] in "AEIOU":
            str.replace(frase,frase[indice],str.lower(frase[indice]))
            indice=indice+1
        else:
            indice=indice+1
    return frase