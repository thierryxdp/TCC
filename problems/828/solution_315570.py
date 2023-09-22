def primo(num):
    """ Dado um número qualquer retorna se determinado número é primo ou não;
    int-> bool """
    lista=[]
    for i in list(range(2,num)):
        if num%i==0 and i!=num:
            lista=lista+[i]
            if len(lista)>0:
                return False
    return True