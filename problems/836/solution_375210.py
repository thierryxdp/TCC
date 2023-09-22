#>>> busca("Contabilidade", matriz)
#>>> [[‘Adalberto Ferreira’, ‘566’, ‘(21)84564-5248’],[‘Flavia Amorim’, ‘465’, ‘(21)2134-4845']]
#Se nenhum registro for encontrado, a função deverá retornar uma lista vazia.


def busca(matriz):
    """Função que receba uma matriz como 
    a do exemplo e faça uma busca por setor, 
    ou seja, dado um nome de um setor da empresa, 
    a função retorna os dados de todos os funcionários 
    daquele setor;
    str -> list"""
    result = []
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz[linha])):
            if area.lower() == matriz[linha][coluna].lower():
                dados = matriz[linha].copy()
                dados.pop(dados.index(dados[coluna]))
                result.append(dados)
                
    return result