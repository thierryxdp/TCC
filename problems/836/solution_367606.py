'''Programa recebe o nome de um setor específico e uma matriz, com uma linha para cada funcionário.
Em cada linha, são especificados nome, registro, setor e telefone do funcionário. A função então verifica
quais dos funcionários estão no setor especificado, e retorna os mesmos.
str, list -> list'''
def busca(setor, matriz):
    contador = 0
    contador1 = 0
    retorno = []
    while len(matriz) > contador:
        if setor in matriz[contador]:
            list.append(retorno, matriz[contador])
            while len(retorno) > contador1:
                list.remove(retorno[contador1], setor)
                contador1 = contador1 + 1
    	contador = contador + 1
    return retorno