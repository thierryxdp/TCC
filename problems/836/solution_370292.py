def busca(setor,matriz):
    """Função que recebe uma matriz e retorna os dados de todos os funcioários daquele
       setor."""
    registro = []
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if setor.lower() == matriz[i][j].lower():
                dados = matriz[i]