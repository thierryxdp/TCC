def primo(num):
    '''Função que recebe um numero inteiro positivo e verifica
       se este número é primo ou não
       : param num: int
       : return: bool
    '''
    lista_de_divisores=[]
    for el in range(1,num+1):
        if num%el==0:
            lista_de_divisores.append(el)
    if len(lista_de_divisores)>2:
        return False
    else:
        return True