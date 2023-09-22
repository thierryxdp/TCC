def busca(funcao,matriz):
    """função que retorna uma lista de contatos com base na busca
    str , list -> list"""
   
    lista_busca = []
    list2=[]
    for lin in matriz:
        for col in lin:
            if col == funcao:
                lin.remove(funcao)
                lista_busca.append(lin)
    			
    return lista_busca