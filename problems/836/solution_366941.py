def busca(m, setor):
    '''Dada uma matriz com os dados dos funcionário de uma empresa,
       a função retorna, quando indicado setor da empresa, quem a 
       ele pertence e seus dados
       list -> list
       Parametros:
       m:lista com dados dos funcionario'''
    l = []
    for c in range(0, len(m)):
        if setor in m[c]:
            l.append(m[c])
    return l