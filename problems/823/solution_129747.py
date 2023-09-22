def faltante(lista):
    NovaLista=[]
    for x in range(1,len(lista)+2):
        NovaLista.append(x)
    for elementoFaltando in NovaLista:
        if elementoFaltando not in lista:
            return elementoFaltando