def intercala(lista1, lista2):
    if lista1 + lista2:
        return intercala(lista1//10, lista2//10) + str(lista1%10) + str(lista2%10)
    else:
        return L3(lista1+lista2)