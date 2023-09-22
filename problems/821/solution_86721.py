def fatorial(num):
    resultado=1
    count=1
    while count <= num:
        resultado *= count
        count += 1
        return(resultado)