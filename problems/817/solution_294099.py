def acima_da_media(m):
    """Função que recebe uma lista e retorna outra com os valores
    acima da media da primeira"""
    media = sum(m)/len(m)
    m2 = [i for i in m if i > media]
    m2.sort()
    return m2