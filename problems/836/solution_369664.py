def busca(setor, matriz):
    """função que dados um nome do setor e uma matriz, retorna os dados de todos os funcionarios daquele setor;str,list-->list"""
    encontrados=[]
    for funcionario in matriz:
        if setor in funciinario[2]:
            encontrados.append(funcionario[:2]+funcionario[3:])
    return encontrados