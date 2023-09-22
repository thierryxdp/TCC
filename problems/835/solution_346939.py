def melhor_volta (matriz):
    """funçao que recebe uma matriz 6x10 no formato lista de listas com o tempo das voltas de corredores em uma corrida e retorna quem teve a melhor participaçao, o tempo da volta e em qual volta foi obtido;
    entrada: list
    saida: tuple (int,int,int)"""
    
    tops = []
    for linha in matriz:
        list.append (tops, min (linha))
    melhor = min (tops)
    corredor = list.index (tops, melhor)
    volta = list.index (linha, corredor)
    
    return (corredor +1, melhor, volta +1)