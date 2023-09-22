def intercala(lista1, lista2):
    " " "Intercala os elementos duas listas de tamanho 3(L1,L2) gerando uma lista L3;lista, lista -> lista" " "
    resposta = []
    resposta = resposta + [lista1[0]]
    resposta = resposta + [lista2[0]]
    resposta = resposta + [lista1[1]]
    resposta = resposta + [lista2[1]]
    resposta = resposta + [lista1[2]]
    resposta = resposta + [lista2[2]]
    return resposta