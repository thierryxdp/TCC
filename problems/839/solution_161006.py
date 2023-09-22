def carros(n,c=5):
    """função que retorna a quantidade de carros necessários para uma viagem, sendo 'n' a quantidade de pessoas e 'c' a capacidade dos veículos. caso a capacidade do carro não seja especificada, será considerada 5. int,int->int"""
    return road(n/c)