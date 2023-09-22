#Pedrinho quer comprar o maior número de bombons possível com o dinheiro que tem
#Faça uma função que calcule o número de bombons, dados o dinheiro e o preço do bombom.
def num_bombons(dinheiro, preco):
    '''  Calcula o número de bombons, dados o dinheiro e o preço do bombom.
    float, float => int, float'''
    quantidade = int (dinheiro/preco)
    return quantidade