def busca(lista,nome):
    i=0
    contatos=[]
    while i<len(lista):
        if str.lower(nome) in str.lower(lista[i][0]):
            contatos=contatos+[lista[i]]
        i=i+1
    return contatos