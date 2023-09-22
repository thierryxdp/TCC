def intercala(L1,L2):
    """Dada duas listas L1 e L2 com o tamanho 3, gera uma lista L3 que é formada intercalando os elementos da L1 e L2. Considere como paramêtro de entrada a lista1 [[1,2,4,16,32,64,-128] e de saída lista2 [3,5,17,33,65,-129]"""
    n1 = len(L1)
    n2 = len(L2)
    i = 0
    j = 0
    L3 = list([])
    while j<n1 and j<n2:
        if lista1[i]<L2[j]:
            L3.append(L1[i])
            i = i+1
        else:
             L3.append(L2[j])
            j = j+1
    while  j<n1:
              L3.append(L1[I])         
             i = i+1
    while j<n2:
             L3.append(L2[j])
            j = j+1
            return L3