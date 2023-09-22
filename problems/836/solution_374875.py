def busca(setor,matriz):
    '''retorna os dados de todos os funcionários do
    setor buscado;entrada-> setor, matriz; 
    str,list(mat)->lista(mat)'''
    resultado = []
    for n in matriz:
        if setor in n:
            resultado= resultado+ [[n[0],n[1],n[3]]]
    return resultado