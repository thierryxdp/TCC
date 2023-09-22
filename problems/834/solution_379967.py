def media_matriz(x):
    nume=0
    den=0
    i=0
    k=0
    while i<len(x):
        den=den+len(x[i])
        i=i+1
    while k<len(x):
        for num in x[k]:
            nume=nume+num
        k=k+1 
    return   round(nume/den,2)