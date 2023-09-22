def carros(p,n=5):
    """função que calcula quantos carros serão necessários
    dados a quantidade de pessoas e a capacidade dos carros"""
    num=p/n
    return math.ceil(num)