def busca(setor, matriz):
    """Função que dado uma matrix contendo os dados dos funcionários de uma empresa, faz uma busca pelo setor dos dados e retorna todos os registros daquele setor. Entrada -> Str and Matrix; Saida -> List"""
    nova_matriz = []
    
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            dados = matriz[i][0:2]+matriz[i][3:]
            nova_matriz = nova_matriz + [dados]
    
    return nova_matriz