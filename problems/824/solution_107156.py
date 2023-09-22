def uppCons(frase):
    """dada uma frase como entrada, a função retorna a mesma frase, porém 
alterando as consoantes para maiúsculas.
str-->str

Parâmetros
frase: frase que terá suas consoantes alteradas para maiúsculas.

    indice=0
    while indice < len(frase):
        if frase[indice] not in "AEIOUaeiouãõáéíóúêâ":
            frase=frase[:indice]+str.upper(frase[indice])+frase[indice+1:]
        indice=indice+1
    return frase