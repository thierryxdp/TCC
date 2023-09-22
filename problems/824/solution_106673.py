def uppCons(frase):
    '''recebe uma frase e retorna a frase com todas as suas consoantes em maiúsculas
    string -> string'''
    indice = 0
    novaFrase = ""
    while indice < len(frase):
        if frase[indice] not in 'AEIOUÁÉÍÓÚáéíóúÂâÃãaeiou':
            novaLetra = str.upper(frase[indice])
            novaFrase = novaFrase + novaLetra
            indice = indice + 1
        else:
            novaFrase = novaFrase + frase[indice]
            indice = indice + 1
    return novaFrase