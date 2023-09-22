def qtd_divisores(n):
    l=list(range(n+1))
    total=0
    for x in l[1:]:
        if n%x==0:
            total+=1
    return total
def primo(n):
    """recebe um número inteiro positivo retorna o valor booleano associado a sua primalidade
    int->bool"""
    if qtd_divisores(n)==2:
        return True
    else:
        return False