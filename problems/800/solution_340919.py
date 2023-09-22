#Questão2
def total(lista,dicionario):
    sigma = 0 
    for coisa in lista:
        if coisa in dicionario:
            sigma += dicionario[coisa]
    return round(sigma,2)