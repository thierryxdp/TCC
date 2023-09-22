def faltante(lista):
    '''diz qual o numero faltando na lista. list->int'''
    a=1
    while a in list:
        a=a+1
    return a