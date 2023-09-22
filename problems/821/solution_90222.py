def fatorial(num):
    ''' Função que recebe um número e calcula seu fatorial
       : param num: int
       : return: int
    '''
    i=1
    fat=1
    while fat<=num:
          i=i*fat
          fat=fat+1
    return i