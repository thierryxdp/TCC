def conta_frases(texto):
    '''A funcao recebe um texto como entrada e retorna o numero
    de frases que estao presentes no mesmo
    str->int'''
    lista=[]
    for i in texto:
        if i=='!':
            lista.append(1)
        if i=='?':
            lista.append(1)
        if i=='.':
            lista.append(1)
        if i=='...':
            lista.append(1)
    return len(lista)+1