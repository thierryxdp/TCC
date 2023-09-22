def busca(string,listaContato):
    lista=[]
    for indice in range(len(listaContato)):
        stringUp=str.upper(string)
        nomeUp=str.upper(listaContato[indice][0])
        if stringUp in nomeUp:
            lista.append(listaContato[indice])
    return lista