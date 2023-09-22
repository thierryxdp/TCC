#Temos como entrada uma lista de numeros e um número n
#Precisamos analisar quais numeros da lista são divisiveis por n
#Quando o numero for divisivel por n, nós o salvamos em uma lista
#Depois retornamos a lista
def filtraMultiplos(lista: list, n:int)-list:
    i=0
    listaMultiplos=[]
    tamanho=len(lista)
    while i < tamanho:
        if lista[i]%n==0:
            listaMultiplos+=lista[i]
        i+=1
    return listaMultiplos