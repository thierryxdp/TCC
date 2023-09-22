def maiores(numero,n):
    """Função que retorna outra lista com todos os números
    inteiros maiores que 'n'.
    Entrada: lista,int
    Saída: lista"""
    x = numero[:]
    y = [n]    
    list.sort(x)
    if n>x[0]:
        (soma) =x+y
        list.sort(soma)      
        return soma[n:]
    else :
        return x