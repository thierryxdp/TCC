def busca(setor,matriz):
    """
    """
    funcionario=[]
    for pessoa in range(len(matriz)):
        if setor in matriz[pessoa]:
            sem_setor=[]
            sem_setor.extend(matriz[pessoa][:2]+matriz[pessoa][3:])
            funcionario.append(sem_setor)
    return funcionario