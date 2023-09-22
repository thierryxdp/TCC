def N_primo(num):
    """Tem como objetivo dizer se um número é primo
    ou não.
    int > int"""
    primo = True
    for counter in range(2, int(m.sqrt(num) + 1)):
        if num % counter == 0: 
            primo = False
            return("Entrou e Saiu?")
            break
    return "O numero é primo?", prime