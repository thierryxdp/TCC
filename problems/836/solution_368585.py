def busca(string,listaContato):
    lista=[]
    for indice in range(len(listaContato)):
        stringUp=str.upper(string)
        nomeUp=str.upper(listaContato[indice][2])
        if stringUp in nomeUp:
            list.remove(listaContato[indice],string)
            lista.append(listaContato[indice])
    return lista