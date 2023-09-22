def media_matriz(matriz):
    """Função que retorna a média de todos os números da matriz de entrada com exatamente duas casas decimais de precisão
list(list) -> float"""

    soma = 0
    qtd_elementos = 0

    for linha in matriz:
        soma = soma + sum(linha)
        qtd_elementos = qtd_elementos + len(linha)
        total = soma / qtd_elementos
    return round(total, 2)