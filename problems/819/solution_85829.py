def filtraMultiplos(lista,n):
    'retorna lista com os multiplos de n'
    'lista,inteiro----lista'
    x=0
    lista_nova=[]
    while x<len(lista):
        if lista[x]%n==0:
            lista_nova+=[lista[x],]
        x +=1
    return lista_nova