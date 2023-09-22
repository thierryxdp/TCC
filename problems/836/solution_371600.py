def busca(funcao,matriz):
   
    lista_busca = []
    list2=[]
    for lin in matriz:
        for col in lin:
            if col == funcao:
                lin.remove(funcao)
                lista_busca.append(lin)
    			
    return lista_busca