def carros(p,c=5):
    '''Calcula o número de carros necessário para uma viagem em grupo, a partir do número de passageiros p e a capacidade dos carros c, sendo a capacidade convencional dos carros de até 5 passageiros e considerando que todos os carros têm igual capacidade; int, int --> int;'''
    return math.ceil(p/c)