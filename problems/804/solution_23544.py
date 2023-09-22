def filtra_pares(a):
    '''Funçao que recebe uma tupla com quatro elementos 
    inteiros como parâmetro, e retorna uma nova tupla 
    contendo apenas os elementos pares da tupla original, na 
    mesma ordem em que se encontravam
    tuple->tuple'''
    lista=[]
    for sub in filtra_pares:
        res=True
        for ele in sub:
            if ele%2!==0:
                res=False
                break
                if res:
                    lista.append(sub)
                    return tuple(lista)