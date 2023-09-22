#Joaozinho quer comprar o maior número de bombons possível com o dinheiro que tem.
#Faça uma função para calcular o número de bombons e o troco, dados o dinheiro e o preço do bombom.
def num_bombons(dinheiro, preço):
    '''  Calcula o número de bombons e o troco, dados o dinheiro e o preço do bombom.
    float, float => int, float'''
    quantidade = int(dinheiro//preço)
    troco = (dinheiro%preço)
    return quantidade, troco