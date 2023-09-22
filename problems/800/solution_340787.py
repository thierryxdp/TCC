def total(ls, d):
    """Somo os produtos especificado em /ls/
    usando o dicionário /d/ como tabela de preços.
    list, dict --> float
    """
    precos = []
    for p in ls:
        list.append(precos, dict.get(d, p, 0))
    return round(sum(precos), 2)