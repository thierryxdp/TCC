def repetidos(lista):
    i=0
    nAnterior=(i+1)
        
    while i<len(lista):
        ocorrencias=0
        if lista[i] == lista[nAnterior]:
            ocorrencias = ocorrencias + 1
        i=i+1
    return ocorrencias