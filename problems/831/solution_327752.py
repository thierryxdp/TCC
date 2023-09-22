def lingua_p(palavra):
    '''Entre com uma palavra para ser retornado a mesma palavra traduzida na
    lingua P
    String -> String'''
    lista1=[]
    lista1[:0]=palavra
    x = lista1.lower()
    y=len(palavra)
    vogal='aeiou'

    for i in len(palavra):
        if i<y:
            if lista1[i] in vogal:
                letra = Npalavra.index(i)
                lista2=lista1.insert(i, "p")
                lista3=lista2.insert(i+1, letra)
                
    return lista3