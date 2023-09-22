def primo (n: int)-> bool:
    '''Retorna 'True' caso o número n seja primo e 'False' caso não seja'''
    for elem in range(n):
        if elem< n and elem != 0 and elem != 1 and n%elem==0:
            return False
    return True