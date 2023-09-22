def busca(setor, matriz):
    """Funcao que, dada um setor e uma lista com os funcionarios 
    de uma empresa retorna as informações dos funcionarios que
    trabalham neste setor.
    Entradas: str, list
    Saida: list"""
    encontrado = []
    
    for linha in range(len(matriz)):
        if matriz[linha][2] == setor:
            encontrado += [[matriz[linha][0], matriz[linha][1], matriz[linha][3]]]
    return encontrado