x = int(input('Dinheiro disponível: '))
y = int(input('Preço do bombom: '))

num_bombons(x, y)

def num_bombons(dinheiro, preco):
    nb = dinheiro/preco
    resto = dinheiro%preco
    print('Será posível comprar' + nb + 'bonsbons. O troco será' + resto + 'reais.')