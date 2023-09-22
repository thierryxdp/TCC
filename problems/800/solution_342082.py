def total(lista,dicio):
    """Função que recebe uma lista de compras e um dicionário contendo o preço de cada
    produto disponível em uma loja, e retorna o valor total dos itens que estejam na lista
    disponíveis nessa loja.
    list,dic->float
    """
    dic = {}
    primeiro = lista
    for primeiro in dicio:
        segundo = list.count(primeiro, dicio)
    terceiro = segundo.values()
    return sum(terceiro)