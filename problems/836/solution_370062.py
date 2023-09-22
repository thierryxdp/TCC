def busca(nome,lista):
    i=0
    contatos=[]
    while i<len(lista):
        if nome in lista[i][0]:
            contatos=contatos+[lista[i]]
        i=i+1
    return contatos