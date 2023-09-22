def busca(setor,funcionarios):

    lista_retorno=[]
    setor=setor.upper()

    for indice,funcionario in enumerate(funcionarios):
        lista_aux=[]
        setor_procura=funcionario[2].upper()
        if setor==setor_procura:
            lista_aux.append(funcionario[0])
            lista_aux.append(funcionario[1])
            lista_aux.append(funcionario[3])
            lista_retorno.append(lista_aux)

    return lista_retorno