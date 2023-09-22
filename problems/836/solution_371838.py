def busca(setor,func):
    '''Função que, dada uma matriz, retorna uma busca por setor.
[Dado o nome de um setor, retorna os dados de todos os funcionários
daquele setor];
str,list->list'''
    lin = len(func)
    col = len(func[0])
    l1 = []
    if setor in func[0]:
        l1 = l1 + func[0]
        l1[0].remove(setor)
        l1 = l1
    if setor in func[1]:
        l1 = l1 + func[1]
        l1[0].remove(setor)
    if setor in func[2]:
        l1 = l1 + [func[2]]
        l1[1].remove(setor)
    return l1