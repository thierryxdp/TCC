def busca(buscasetor,matriz):
    '''Função que dados o setor e uma matriz com informações, retorna as informções do de
    todos os funcionários do mesmo setor. As informações por linha são: nome, registro
    setor e telefone Entrada: str. Saída list'''
    lista=[]
    for infos in matriz:
        if str.lower(buscasetor)==str.lower(infos[2]):
            list.append(lista,[infos[0],infos[1],infos[3]])
    return lista