def busca (setor,m):
    '''recebe uma matrix e busca por setor, retornando os dados dos funcionarios do setor'''
    '''str,list->list'''
    
    tupla = []
    
    for n in m:
        for i in n:
            if i ==setor:
                indice = list.index (n,i)
                del n [indice]
                tupla += [n,]
    return tupla