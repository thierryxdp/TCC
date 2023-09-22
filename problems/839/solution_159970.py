def carros (passageiros,capacidade=5):
    '''Função para apresentar quantos carros serão necessários para fazer a viagem'''
    if passageiros%capacidade == 0:
        return passageiros//capacidade
    else:
        return passageiros//capacidade + 1