def carros(n,c=5):
    """calcula a quantidade necessária de carros de acordo com o número  n de pessoas e a capacidade c do carros; caso a capacidade não seja informada será atribuido o valor 5"""
    return math.ceil(n/c)