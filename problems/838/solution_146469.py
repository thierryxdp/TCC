def num_bombons(dinheiro, preco):
    nb = dinheiro/preco
    resto = dinheiro%preco 
    return 'Será posível comprar' + nb + 'bonsbons. O troco será' + resto + 'reais.'

num_bombons(12, 5)