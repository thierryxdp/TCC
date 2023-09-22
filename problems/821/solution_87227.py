def fatorial(numero):
    """Função que dado um número, calcula o faotiral deste número.
       int -> int
       
       Parâmetros: 
       numero: número que será calculado o fatorial.
       
       returns: O fatorial do número dado.
    """
    contador = 0
    fatorial = 1
    while contador < numero:
        fatorial = fatorial*numero
        numero = numero - 1
    return fatorial