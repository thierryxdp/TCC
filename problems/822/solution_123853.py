def repetidos(numeros):
    '''retorna a quantidade de vezes que um numero e igual ao
    anterior;
    list->int'''
    i=1
    reps=[]
    while i<=len(numeros):
        if int(numeros[i])==int(numeros[i-1]):
            list.append(reps,'avante')
        i=i+1
    return len(reps)