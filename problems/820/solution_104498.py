def posLetra(string, letra, numero):
    """Função que recebe como entrada uma string, uma letra, e um número que
    indica a ocorrência desejada da letra (1 para 1ª ocorrência, 2 para 2ª,
    etc). A função deve retornar em que posição da string aquela ocorrência
    da letra está. Caso exista menos ocorrências da letra do que a ocorrência 
    pedida, a função deve retornar -1;
    str, str , int -> int"""
    contador = 0
    indice = 0
    ocorrencia = 0
    lista = list(string)
    while contador < len(lista):
        if lista[indice] == letra:
            ocorrencia += 1
            if ocorrencia == numero:
                return indice

        contador += 1
        indice += 1

    return -1