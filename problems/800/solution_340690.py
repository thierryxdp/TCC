def total(produtos,lista):
    soma=0
    for comida in produtos:
        if comida in lista:
            soma=soma+lista[comida]  
    return soma