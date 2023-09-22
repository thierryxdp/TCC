def uppCons(frase):
    """Dada uma frase, a função vai retornar uma nova frase com
    todas consoantes em maiúsculas e manter as vogais em letras
    minúsculas.
       A frase deve ser escrita entre aspas;
       str --> str"""
    novaFrase = ""
    indiceLetra = 0
    while indiceLetra < len(frase):
        if frase[indiceLetra] in "bcdfghjklmnpqrstvwxyzç":
            novaFrase = novaFrase + str.upper(frase[indiceLetra])
        else:
            novaFrase = novaFrase + frase[indiceLetra]
        indiceLetra = indiceLetra + 1
    return novaFrase