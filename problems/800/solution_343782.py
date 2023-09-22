# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total (lista,dicionario):
    """Função que dada uma lista de compras e um dicionário com o preço de cada produto disponível em uma determinada loja, ira retornar o valor total, dos produtos da lista de compras que estejam disponíveis."""
    valores = []
    for produto in lista:
        if produto in dicionario:
            valores.append(dicionario.get(produto))
    return round(sum(valores),2)