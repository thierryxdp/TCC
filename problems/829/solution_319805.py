def soma_h(n):
    """Função que soma o conjunto 1 sobre 1 até 1 sobre 'n' passando por
    todos os inteiros no caminho;
    int -> float"""
    soma=0
    for e in range(1, n+1):
        soma+= 1/e
    return round(soma,2)