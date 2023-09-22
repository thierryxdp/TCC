def melhor_volta (matriz):
    """funçao que recebe uma matriz 6x10 no formato lista de listas com o tempo das voltas de corredores em uma corrida e retorna quem teve a melhor participaçao, o tempo da volta e em qual volta foi obtido;
    entrada: list
    saida: tuple (int,int,int)"""
    
    menor = min (matriz)
    for linha in matriz:
        for coluna in linha:
            if coluna == menor:
                return (linha, menor, coluna)