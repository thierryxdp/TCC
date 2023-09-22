def carros(pessoas,capacidade=5):
    '''A função retorna o número exato de carros necessários
    para se fazer uma viagem, dado o número de pessoas.
    Caso a capacidade dos carros não seja informada, a função
    assume a capacidade convencional de 5 pessoas por veículo.
    int, int -> int'''
    if (pessoas%capacidade==0):
        return pessoas/capacidade
    else:
        return (pessoas//capacidade+1)