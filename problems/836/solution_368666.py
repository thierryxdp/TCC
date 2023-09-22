def busca(setor, matriz):
    '''retorna os dados dos funcionaios que trabalham no setor
    fornecido. Retorna uma lista vazia caso nenhum trabalhe;
    str, list -> list'''
    j=0
    lista_retorno=[]
	while j<len(matriz):
        if matriz[j][2]==setor:
            lista_retorno=lista_retorno+[matriz[j][0]+matriz[j][1]+matriz[j][3]+)]
        j=j+1
    return lista_retorno