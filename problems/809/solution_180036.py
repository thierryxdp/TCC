def intercala(lista1, lista2):
    inter = lista1[0:1] + lista2[0:1] + lista1[1:2] + lista2[1:2]
    inter2 = lista1[2:3] + lista2 [2:3] + lista1[3:] + lista2[3:]
    intercala = inter + inter2
    return intercala