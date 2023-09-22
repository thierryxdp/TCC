def busca(setor,matriz_func):
    """Essa funcao recebe uma matriz e faz uma busca por setor, ou seja, dado um nome de um setor da empresa,a funcao retorna os dados de todos os funcionarios daquele setor;
str, list-> list"""
    lista_retorno = []
    for i in range(len(matriz_func)):
        if setor==matriz_func[i][2]:
            lista_retorno.append(matriz_func[i][:2]+matriz_func[i][3:])
            if lista_retorno == []:
                return "Nenhum registro encontrado!"
            return lista_retorno