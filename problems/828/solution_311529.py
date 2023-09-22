def primo(x):
    '''função que,dado um inteiro positivo, verifica se ele é primo ou não,
    retornando True caso seja e False caso não; int -> str'''
    lista=[]
    for i in range(1,x+1):
        if x%i == 0:
            list.append(lista,i)
    if len(lista) > 2 :
        return False
    else:
        return True