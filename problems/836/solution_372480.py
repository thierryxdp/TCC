def busca(setor,matriz):
    """Primeiramente, é criada uma lista vazia onde ficarão os dados
    dos funcionários do setor. Para cada pessoa/linha da matriz, é verificado
    se nos dados dessa pessoa se encontra o setor buscado.
    Caso não, nada ocorre, caso sim, é criada uma lista vazia onde o nome, registro e
    telefone da pessoa são adicionados, evitando modificar a matriz original.
    E essa lista é adicionada a lista dos funcionários do setor. Após verificar
    para toda linha da matriz, retorna a lista completa com os funcionários do setor.
    """
    funcionario=[]
    for pessoa in range(len(matriz)):
        if setor in matriz[pessoa]:
            sem_setor=[]
            sem_setor.extend(matriz[pessoa][:2]+matriz[pessoa][3:])
            funcionario.append(sem_setor)
    return funcionario