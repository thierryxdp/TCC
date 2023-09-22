def inverte(string):
    minusculo= string.lower()
    lista= minusculo.split()
    frase = lista[::-1]
    str1=', '.join(frase)
    sem_pont= str1.replace(', ' , ' ' ,10)
    return sem_pont