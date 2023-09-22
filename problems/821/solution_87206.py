def fatorial(num):
    """Cálculo de uma função que dado um número calcula a fatorial desse numero. 
    
       Parameters:
       num: numero a ser calculado
       
       Returns:
       Retorna a fatorial do numero, dado que:
       int -> int 
    """
    mult=1
    c=1
    lista_f=list(range(num+1))
    while c<len(lista_f):
        mult=mult*lista_f[c]
        c=c+1
    return mult