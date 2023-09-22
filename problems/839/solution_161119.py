def carros(x,y=5):
    '''função que calcula a quantidade de carros necessários para x pessoas em
    carros de capacidade y fazerem uma viagem rodoviária, se y n for determinado y=5'''
    return ceil(x/y)