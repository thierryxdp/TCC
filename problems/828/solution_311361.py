def primo (n):
    """Função que dado um numero, retorna se esse numero é primo ou não;
       int -> bool."""
    quantidade= []
    for numero in list (range (1, n+1)):
        if n % numero == 0:
            list.append (quantidade, numero)
    if len (quantidade) == 2:
        return True
    else:
        return False