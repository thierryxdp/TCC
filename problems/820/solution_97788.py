def posLetra(frase,let,num):
    '''Função que indica a ocorrência desejada de uma letra let 
    em uma string frase. Caso exista menos ocorrências da letra do
    que a ocorrência pedida, a função retornará -1.
    frase=str,let=str,num=int->int'''
    x=list(frase)
    y=list.count(x,let)
    z=0 
    h=list.index(frase,let,num)
    n=1
    if num<y or y==0:
        return -1
    while n < num:
        z=h+1
        n=n+1
    return h