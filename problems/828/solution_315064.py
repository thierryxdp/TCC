def qtd_divisores(n):
    """Retorna quantas divisões um numero tem. int -> int"""
    lista = []
    for a in range(1,n+1): 
        if n%a == 0: 
            list.append(lista,a)
    return len(lista)
def primo(n): 
    """Retorna um valor boolenao indicando se o número dado como entrada é primo
       int->bool"""
    if qtd_divisores(n)==2: 
        return True
    else: 
        return False