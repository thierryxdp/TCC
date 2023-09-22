def busca(s:str,matriz:list)->list:
    """dado o nome de um setor da empresa, a funçao retorna uma lista com osdados de todos os funcion´arios daquele setor"""
    lista_retorno=[]
    for i in matriz:
        if i[2]==s:
            lista_retorno.append(i[0,2]+i[3:])
    return lista_retorno