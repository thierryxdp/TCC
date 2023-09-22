def fatorial(numero)
    '''funcao que fatora um numero'''
resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1

return(resultado)