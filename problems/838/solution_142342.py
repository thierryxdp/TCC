#Joaozinho quer comprar o maior número de bombons possível com o dinheiro que tem
#Faça uma função para calcular o número de bombons, dados o dinheiro e o preço do bombom.
def num_bombons(dinheiro, preço):
    '''  Calcula o número de bombons, dados o dinheiro e o preço do bombom.
    int => int'''
    quantidade = int(dinheiro//preço)
    return