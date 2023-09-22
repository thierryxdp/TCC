def melhor_volta (matriz):
    """funçao que recebe uma matriz 6x10 no formato lista de listas com o tempo das voltas de corredores em uma corrida e retorna quem teve a melhor participaçao, o tempo da volta e em qual volta foi obtido;
    entrada: list
    saida: tuple (int,int,int)"""
    
    menor = min (matriz)
    melhor = ()
    for linha in matriz:
        pos = 0
        while linha[pos] != menor:
            pos = pos +1
                
    return (linha, menor, linha[pos])