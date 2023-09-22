def posLetra (frase, letra, ocorrencia):
    """Função que dado uma string(frase), uma letra(letra) e um número de
    ocorrências(ocorrencia) e retorna a posição da string aquela ocorrência
    da letra está.
    str, str, int -> int"""
    indice = 0
    contador = 0
    while(indice < len(frase)):
        if letra in frase[indice]:
            j += 1
        indice += 1

    if j == ocorrencia:
        return indice - 1

    else:
        return -1