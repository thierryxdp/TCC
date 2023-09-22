def lingua_p(frase):
    """A funcao traduz uma frase para a lingua do p, que consiste em trocar 
    as vogais por p e em seguinda ter a vogal trocada, inserida antes e depois do p, por exemplo vogal retirada "o"
    ,sera substituido por "opo". str-->str"""
    frase = frase.lower()
    lista = list(range(len(frase)))
    lista[:] = frase
    for i in range(len(lista)):
        if lista[i] not in " bcdfghjklmnpqrstvwxyz":
            lista[i] = lista[i]+ "p" + lista[i]
    return str.join("",lista)