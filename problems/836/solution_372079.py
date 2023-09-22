def busca(setor, matriz):
    '''retorna uma matriz com os dados dos funcionarios
       de um certo setor dado, e uma matriz
       str, list -> list'''
    
    lista=[]
    a=[]
    
    for i in matriz:
        if setor in i:
            a=list.remove(i, setor)
            lista+=a
            
    return lista