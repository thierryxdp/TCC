def busca(funcao,matriz):
   
    lista_busca = []
    list2=[]
    for lin in matriz:
        for col in lin:
            if col == funcao:
                
                lista_busca.append(lin.remove(funcao))
    			
    return lista_busca