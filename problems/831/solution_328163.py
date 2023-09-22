def lingua_p(palavra):
    palavra2=str.lower(palavra)
    lista=list(palavra2)
    vogais=['a','e','i','o','u']
    lista2=[]
    lista3=[]
    string=''
    for var in range(len(lista)):
        if lista[var] in vogais:
            list.append(lista2,var)
            list.append(lista3,lista[var])
    for k in range(len(lista2)):
        posicao=lista2[k]
        lista[posicao]=str(lista3[posicao])+'p'+str(lista3[posicao])
    for i in range (len(lista)):
        string=string+lista[i]
    return string