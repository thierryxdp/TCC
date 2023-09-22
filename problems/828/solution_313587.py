def primo(n):
    """funcao que dado um nuemro inteiro e positivo, verifica se é primo ou nao
    e retorna true se for primo, e se nao for retorna false. int->bool."""
    soma=1
    lista=[]
    while soma<=n:
        if n%soma==0:
            list.extend(lista,[soma])
        soma += 1
    if len(lista)==2:
        return True
    return False