def repetidos(lista):
    '''dada uma lista de números, retorna o número de repetições presentes nela
list-->int'''
    i=0
    repeticoes=0
    while i+1<len(lista):
        if lista[i]==lista[i+1]:
            repeticoes+=1
        i+=1
    return repeticoes