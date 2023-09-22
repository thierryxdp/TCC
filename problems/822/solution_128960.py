def repetidos(lista):
    i=0
    nAnterior=(i-1)
    ocorrencias=0
    
    while i<len(lista):
        if lista[i] == lista[nAnterior]:
            ocorrencias = ocorrencias + 1
        i=i+1
    return ocorrencias