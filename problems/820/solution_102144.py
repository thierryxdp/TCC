def posLetra(frase, letra, num):
    if(list.count(list(frase), letra))< num:
        return -1
    lista = []
    contador = 0
    while contador < len(frase):
        if str(letra) in frase[contador]:
            lista.append(contador)
        contador += 1
        if len(lista) > num:
            del lista[num:]
    return lista[-1]