def busca(funcao,matriz):
   
    lista_busca = []
    list2=[]
    for lin in matriz:
        for col in lin:
            if col == funcao:
                list2 = lin.remove(funcao)
                lista_busca.append(list2)
    			
    return lista_busca