def busca(setor,matriz):
    '''A partir dos dados dos funcionarios na matriz retorna
    as informacoes dos que trabalham no setor fornecido
    como entrada
    str,list -> list'''
    resultado = []
    for funcionario in matriz:
        if setor in funcionario:
            del funcionario[2]
            list.append(resultado,funcionario)
    return resultado