def primo(n):
    '''Função que retorna true caso um numero seja primo
    e false caso não seja. int -> bool'''
    lista = []
    for x in list(range(1,n+1)):
                  if n%x == 0:
                      lista = lista + [x]
    if len(lista) == 2:
        return True
    else:
        return False