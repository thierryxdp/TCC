def faltante(L):
    #Essa função irá descobrir qual número inteiro está faltando no intervalo
    #Entrada: lista | Saída: Inteiro
    lista= list(range(1,len(L)+5))
    index = 0
    list.extend (L, [0,0,0])
    while lista[index]==L[index]:
        index=index+1
    return lista[index]