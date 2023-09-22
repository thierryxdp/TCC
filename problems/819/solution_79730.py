# A função recebe uma lista de números e um número n, e retorna outra lista contendo todos
# os números da lista original que forem divisíveis por n.
# list,int->list
# div: lista dos números divisíveis por n
def filtraMultiplos(lista,n):
    i=0
    div=[]
    while i < len(lista):
        if lista[i]%n==0:
            list.append(div,lista[i])
        i=i+1
    return div