def busca(setor:str,matriz_1:list)->list:
    matriz_do_setor = list(filter(lambda x: setor in x, matriz_1))
    def retira_setor(matriz_2:list)->list:
        matriz_2.remove(setor)
        return matriz_2
    return list(map(retira_setor,matriz_do_setor))