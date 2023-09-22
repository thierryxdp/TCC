def melhor_volta(matriz:list)->tuple:
    """Dada uma matriz 6x10 (6 jogadores e 10 voltas) com cada tempo em segundos,
       informa quem fez a melhor volta, em qual tempo e qual volta. 
       Os jogadores variam de 1 a 6 e as voltas de 1 a 10.
       
       Parameters:
       matriz: matriz 6x10, cada linha é de um jogador e cada coluna uma volta
       
       Returns:
       quem fez a melhor volta, em qual tempo (em segundos) e qual volta
    """
    
    linha = len(matriz)
    coluna = len(matriz[0])
    
    menortempo_jogador = []
    jogador = list.index(menortempo_jogador,min(menortempo_jogador)) + 1
    volta = list.index(matriz[jogador-1],min(menortempo_jogador)) + 1
    
    for i in range(linha):
        list.append(menores_tempos, min(matriz[i]))
    return(jogador, min(menortempo_jogador), volta)