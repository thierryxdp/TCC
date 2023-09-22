def total(lis,mydic):
    """ A função retorna o valor total dos produtos disponíveis de uma lista;
    list, dict -> float """
    vtotal = 0
    for prod in lis:
        vtotal+=mydic[prod]
    return round(vtotal,3)