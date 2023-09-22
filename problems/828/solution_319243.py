def primo(n):
    """Função que verifica se o número recebido é primo ou
    não;
    int -> bool."""
    div = [1]
    primo = [1,n]
    if n == 1:
        return True
    for e in range(2,n+1):
        if n % e == 0:
            div.append(e)
    return div == primo