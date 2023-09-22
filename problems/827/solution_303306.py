def qtd_divisores (n):
    """Função que conta quantos divisores um dado numero tem;
       int -> int."""
    divisiveis= []
    for numero in list (range (1,n+1)):
        if n % numero == 0:
            list.append (divisiveis, numero)
    return len (divisiveis)