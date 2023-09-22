def carros(npessoas:int,capacidade=5)->int:
    '''A função carros retorna a quantidade de carros necessárias para transportar determinada
    quantidade de pessoas de acordo com a capacidade de cada carro. Sendo a capacidade não informada,
    o programa assumirá que ela é padrão (5). Assim, ele retornará considerando a capacidade de veículos
    convencionais e não convencionais.'''
    return math.ceil(npessoas/capacidade)