def substitui(s,x,i):
    '''Função que nos retornará uma string s onde a posição i será substituido por x'''
    palavra=s
    inteiro=int(i)
    troca= (inteiro+1)
    return palavra[:i]+str(x)+palavra[troca:]