def lingua_p(palavra):
    '''Entre com uma palavra para ser retornado a mesma palavra traduzida na
    lingua P
    String -> String'''
    Npalavra=palavra
    x = Npalavra.lower()
    lista1=[]
    lista1[:0]=Npalavra
    y=len(palavra)
    vogal=["a", "e", "i", "o", "u"]

    for i in range(len(palavra)):
        if i<y:
            if lista1[i] in vogal:
                letra=lista1[i]
                z=lista1.index(i)
                lista2=lista1.insert(i, "p")
                lista3=lista2.insert(i+1, letra)
                
    return lista3