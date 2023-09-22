#Função para calcular o número de divisores
def qtd_divisores(n):
    #int --> int
    numdiv=0
    for i in range(1,n+1):
        if n%i==0:
            numdiv=numdiv+1
    return numdiv

#Função que verifica se é primo, ou seja, se possui dois divisores
def primo(n):
    #int --> bool
    if qtd_divisores(n)==2:
        return True
    return False