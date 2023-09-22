def total(produtos,lista):
    soma=0
    i=0
    for comida in produtos:
        if comida in lista:
            soma=soma+comida
        i=i+1    
    return soma