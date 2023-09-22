def repetidos(lista):
    """Dado como entrada uma lista contendo números inteiros positivos,
    retorna quantas vezes o n-(ésimo-1) número é igual ao n-ésimo;
    lista(int)->int"""
    i=1
    s=0
    while i<len(lista):
        if lista[i-1]==lista[i]:
            s+=1
        i+=1
    return s