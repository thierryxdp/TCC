def num_bombons (x, y):
    """Calcula quantos bombons possiveis dados o dinheiro e o preço do bombom;
int, int -> int"""
    if x//y == 1:
        return str(1) + ' bombom'
    else:
        return str (x//y) + ' bombons'