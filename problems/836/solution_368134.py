def busca(string,listaContato):
    lista=[]
    for indice in range(len(listaContato)):
        stringUp=str.upper(string)
        nomeUp=str.upper(listaContato[indice][2])
        if stringUp in nomeUp:
            lista.append(listaContato[indice])
    return lista