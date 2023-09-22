def intercala(lista1,lista2):
    """Dada a lista1 e lista2, retorna uma lista3 formada pelos elementos de lista1 e lista3"
    "int,int,int + int, int,int --->int,int,int,int,int,int.""" 
    [a,b,c] = lista1
    [d,e,f] = lista2
    lista3 = [a] + [d] + [b] + [e] + [c] + [f]
    return lista3