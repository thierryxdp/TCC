def qtd_divisores(n):
    """Função que dado número n retorna a quantidade de divisores que este possui;
    int->int"""
	l=range(n+1)
    k=0
    for x in l[1:]:
        if n%x==0:
            k=k+1
    return k
def primo(n):
    """Retorna um valor booleano para a pergunta se n é um número primo;
    int->bool"""
    if qtd_divisores(n)==2:
        return True
    else:
        return False