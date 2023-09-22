def busca(setor,matriz):
    '''função que recebe uma string e uma matriz e reorna os dados de todos os funcionarios do setor dado pela string.
    str, list -> list
    explicação: percorre a matriz, identificaa se o setor bate, se sim vai usando esses que tem o mesmo setor retirando a palavra que corresponde ao setor.'''
	lista = []
    for c in matriz:
        if c[2] == setor:
            list.append(lista, c)
    		list.remove(c,setor)
    return lista