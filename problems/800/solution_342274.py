# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista,dicio):
    """Função que recebe uma lista, verifica no
    dicionario o valor dos itens na lista e
    retorna o valor total da lista com duas casas decimais
    list, dic -> float"""
    tot = 0
    for cb in lista:
        tot = tot + dicio[cb]
    return round(tot,2)