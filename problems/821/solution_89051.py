def fatorial(n):
    tupla = [n]
    while n != 1:
        n = n - 1
        tupla += [n,]
    
    tupla2 = str.split(tupla,',')
    return tupla2