def posLetra(string, letra, n):
    """
    Essa função recebe uma string, uma letra e um número da ocorrência 
    desejada da letra, retornando qual a posição na string em que 
    aquela ocorrência da letra está;
    str, str, int -> int
    """
    lista = []
    contador = 0
    for x in string:
        if x == letra:
            lista.append({x: contador})
        contador +=1
    if n > len(lista):
        return -1
    dicionario = lista[n-1]
    resultado = dicionarios.values()
    for y in resultado:
        return y
    return -1