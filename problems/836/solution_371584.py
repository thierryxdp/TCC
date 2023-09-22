def busca(funcao,matriz):
   
    lista_busca = []
    for lin in matriz:
        for col in lin:
            if col == funcao:
                lista_busca.append(lin)
    			lista_busca.remove(funcao)
    return lista_busca