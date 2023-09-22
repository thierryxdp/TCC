def busca(setor,matriz):
    """Função que dada uma matriz com as informações dos funcionários,
       faça uma busca por setor.
       
       Parameters:
       setor: Setor que queremos identificar
       matriz: Matriz com as informações dos funcionários
       
       Returns:
       Retorna os dados dos funcionários daquele setor.
       str, list -> list
       """
    lista = []
    for i in range(len(matriz)):
        if matriz[i][1] == setor:
            list.remove(matriz[i],setor)
            list.append(lista,matriz[i])
    return lista