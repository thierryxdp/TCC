def conta_numero(numero,matriz):
    '''função retorna quantas vezes um número aparece 
    na mmatriz. int,list --> int'''
    i = 0 
    for item in matriz:
        for item_2 in item:
            if item_2 == numero:
                i +=1
    return i