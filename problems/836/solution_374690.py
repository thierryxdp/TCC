def busca(setor, dados):
	'''
    Dado um string com o nome de um setor da empresa e uma matriz contendo
    os dados dos funcionários de cada setor, retorna uma matriz com os dados dos
    funcionários do setor pesquisado
    
    str, list -> list
    '''
    dados_setor=[]
    i=0
    while i<len(dados):
        if dados[i][2]==setor:
            dados_setor.append([dados[0],dados[1],dados[3]])
        i+=1
    return dados_setor