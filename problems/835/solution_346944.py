def melhor_volta (matriz):
    """funçao que recebe uma matriz 6x10 no formato lista de listas com o tempo das voltas de corredores em uma corrida e retorna quem teve a melhor participaçao, o tempo da volta e em qual volta foi obtido;
    entrada: list
    saida: tuple (int,int,int)"""
    
    melhores = []
    for linha in matriz:
        list.append (melhores, min (linha))
    top = min (melhores)
    corredor = list.index (melhores, top)
    volta = list.index (matriz[corredor], top)
    
    return (corredor +1, top, volta +1)