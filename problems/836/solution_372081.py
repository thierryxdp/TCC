def busca(setor, matriz):
    '''retorna uma matriz com os dados dos funcionarios
       de um certo setor dado, e uma matriz
       str, list -> list'''
    
    lista=[]
    
    for i in matriz:
        if setor in i:
            list.remove(i, setor)
            lista+=list(i)
            
    return lista