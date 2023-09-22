def repetidos (lista):
    '''primeiro comparando com o termo anterios e determinando
    que a contagem começara do 1 porque se começar do 0 não tem 
    coerencia e não esquecendo do contador para contar
    as repetições'''
    i=1
    c=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            c+=1
        i+=1
    return c