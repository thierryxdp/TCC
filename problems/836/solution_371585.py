def busca(funcao,matriz):
   
    lista_busca = []
    for lin in matriz:
        for col in lin:
            if col == funcao:
                lista_busca.append(lin)
    			
    return lista_busca