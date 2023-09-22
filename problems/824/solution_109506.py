def uppCons(frase):
    """Função que dada uma frase, retorna a frase onde todas as consoantes são maíusculas (e os demais caracteres continuam exatamente como na frase original).
    str -> str """

    lista = list(frase)

    i = 0
    while i <= len(lista) - 1:
        if lista[i] not in 'AEIOUaeiouÃÕÂÊÎÔÛÁÉÍÓÚ':
            lista[i] = str.upper(lista[i])

        i = i + 1

    frase_consoante_maiuscula = str.join("", lista)

    return frase_consoante_maiuscula