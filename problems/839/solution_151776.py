#funcao q retorna um numero exato de carros para grupos de amigos, lembrando q em cada carro pode entrar até 5 pessoas
def carros(gnt):
    """ dado um numero de pessoas retorna a quantidade de carros
    int - int"""
    return math.ceil(gnt / 5)