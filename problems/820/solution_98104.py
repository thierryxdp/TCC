def posLetra (frase, letra, ocorrencia):
    """Função que dado uma string(frase), uma letra(letra) e um número de
    ocorrências(ocorrencia) e retorna a posição da string aquela ocorrência
    da letra está.
    str, str, int -> int"""
    indice = 0
    contador = 0
    while(indice < len(frase)):
        if letra in frase[indice]:
            contador += 1

        if contador == ocorrencia:
            return indice

        indice += 1

    return -1