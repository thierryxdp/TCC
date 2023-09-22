def primo(n):
    
# retorna True se um número for primo e False se não for primo, dado um número inteiro n

    lista = []

    for i in range(1,n+1):
        if n % i == 0:
            lista.append(i)

    if len(lista) > 2:
        return False

    if lista[0] == 1 and lista[1] == n:
        return True