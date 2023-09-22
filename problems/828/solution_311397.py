def primo(n):
    """ Retorna True caso n seja um número primo e False caso ele não seja; int -> bool """
    lista_divisores=[]
    for i in range(1,n+1):
        if n%i==0:
            list.append(lista_divisores,i);
    if len(lista_divisores)>2:
        return False;
    else:
        return True