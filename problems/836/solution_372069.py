def busca(setor, func):
    """função que busca funcionários dado uma matriz do setor"""
    lin = len(func)
    col = len(func[0])
    l1 = []
    if setor in func[0]:
        l1 = l1 + [func[0]]
        l1[0].remove(setor)
        l1 = l1
    if setor in func[1]:
        l1 = l1 + [func[1]]
        l1[0].remove(setor)
    if setor in func[2]:
        l1 = l1 + [func[2]]
        l1[1].remove(setor)
    return l1