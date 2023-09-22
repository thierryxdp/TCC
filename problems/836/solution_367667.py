def busca(texto,lista):
    """Dada uma lista de informacoes de contatos de funcionarios e o setor de uma empresa, retorna as informacoes de todos os contatos desse setor"""
    """entrada: lista(lista), str
    saida:lista"""
    
    lista1 = lista[:]
    
    resultado = []

    for pos in range(len(lista1)):
        if str.lower(texto) in str.lower(lista1[pos][2]):
            list.append(resultado,lista[pos][0])
            list.append(resultado,lista[pos][1])
            list.append(resultado,lista[pos][3])

        pos=pos+1

    return resultado