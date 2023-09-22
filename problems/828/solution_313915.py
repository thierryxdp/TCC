def primo(n):
    """funcao que dado um nuemro inteiro e positivo, verifica se é primo ou nao
    e retorna true se for primo, e se nao for retorna false. int->bool."""
    soma=1
    lista=[]
    for primo in range(1,n+1):
        if n%primo==0:
            list.extend(lista,[primo])
    if len(lista)==2:
        return True
    return False