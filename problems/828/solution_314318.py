def soma_primos(n):
    """..."""
    i = 1
    numero_primos = 0
    while numero_primos<n:
        if primo(i): 
            numero_primos = numero_primos+1
        i = i+1
    return numero_primo