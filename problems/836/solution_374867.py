def busca(string,matriz):
    'Função que recebe o nome de um setor e uma matriz e faz a busca pelas informações dos funcionários desse setor, retornando-as.'
    'str,list->list'
    
    lista=[]
    for linha in matriz:
        for informacao in linha:
            if string in informacao:
                lista=lista+[linha]

    for funcionario in lista:
        list.remove(funcionario,string)

    return lista