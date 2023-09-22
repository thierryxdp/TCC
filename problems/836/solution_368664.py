def busca(setor, matriz):
    '''retorna os dados dos funcionaios que trabalham no setor
    fornecido. Retorna uma lista vazia caso nenhum trabalhe;
    str, list -> list'''
    j=0
    lista_retorno=[]
	while j<len(matriz):
        if matriz[j][2]==setor:
            lista_retorno=lista_retorno+[list.remove(matriz[j],setor)]
        j=j+1
    return lista_retorno