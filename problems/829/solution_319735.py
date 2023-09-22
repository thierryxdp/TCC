def soma_h(n):
    '''Dada um número n inteiiro soma todos os inversos de 1 ate n
    int -> float'''
    h = 0
    for i in range(1, 1 + n):
        h += 1 / i
    return round(h,2)