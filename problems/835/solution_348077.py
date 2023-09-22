def melhor_volta(matriz):
    """ função que recebe uma matriz 6x10 de entrada, que corresponde a seis corredores, com seus tempos nas 10 voltas e retorna quem foi o melhor corredor, com o melhor tempo, na melhor volta
        entrada: lista
        saida: tupla
    """
    contador = 0
    lista1 = []
    lista_final = []
    
    for lista in range(matriz): 
        lista1 = min(lista [::])