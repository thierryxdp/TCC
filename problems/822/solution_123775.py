def repetidos(lista_numeros):
    '''retorna quantos números são repetidos sequencialmente
       list -> int'''

    i = 1
    j = 0
    x = []
    y=[]
    repeticoes = 0

    while i<len(lista_numeros):
        if lista_numeros[i]==lista_numeros[i-1]:
            repeticoes +=1
        i += 1
    return repeticoes