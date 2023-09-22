def busca(setor, matriz):
    ''' 
    Dado uma matriz realiza uma busca por setores

    Uso:
   busca(setor, matriz)

    Entrada:
    - setor (srt): Setor de trabalho para realizar a busca
    - matriz (list): Matriz de informação

     Saída:
    - Retorna os dados de todos os funcionários de um determinado setor de entrada. (list)    
    '''
    y=[]
    for i in range (len(matriz)):
        if setor in matriz [i]:
            matriz[i].remove(setor)
            y=y+[matriz[i]]
    return y