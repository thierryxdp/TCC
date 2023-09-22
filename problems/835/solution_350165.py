def melhor_volta(matriz):
    """Dada uma matriz que representa os corredores, o tempo e
    as voltas de cada corredor numa pista de kart, a função irá
    encontrar quem obteve o menor tempo da corrida e irá retornar
    qual foi o corredor, o tempo que ele fez, e em qual volta
    Tipo da variável matriz: list
    Tipo da saída: list"""
    checagem = 100
    for contador in range(6):
        for contagem in range(10):
            if matriz[contador][contagem] < checagem:
                checagem = matriz[contador][contagem]
                voltas = (contador+1, matriz[contador][contagem], contagem+1)
	return voltas