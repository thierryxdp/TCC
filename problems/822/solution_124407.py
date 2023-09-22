def repetidos(lista):
    """Dada uma lista de numeros, retorna a quantidade de 
    vezes que alguns forans repetidos list - > int """
    rep = []
    i = 0
    while i < len(lista)-1:
        
        if lista[i]==lista[i+1]:
            list.append(rep,lista[i])
        i = i + 1
    return len(rep)