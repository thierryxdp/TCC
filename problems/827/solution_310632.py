def Divisores(m):
    divs = [1]; 
    for i in range(2, m//2 + 1):
    if m%i == 0:
        divs.append(i)
        divs.append(m)
        return divs