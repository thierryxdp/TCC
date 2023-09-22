def busca(setor,matriz):
    '''A partir dos dados dos funcionarios na matriz retorna
    as informacoes dos que trabalham no setor fornecido
    como entrada
    str,list -> list'''
    resultado = []
    for funcionario in matriz:
        copia = list.copy(funcionario)
        if setor in copia:
            del copia[2]
            list.append(resultado,copia)
    return resultado