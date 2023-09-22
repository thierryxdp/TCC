def repetidos(numero):
    m = 0
    n = 0
    while n< len(numero)-1:
        if numero[n+1] == numero[n]:
            m= m +1
            n = n+ 1
        if numero[n+1] != numeor[n]:
            n = n +1 
    return m