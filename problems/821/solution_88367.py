def fatorial(numero):
    """Função que calcula o fatorial do número dado como entrada
int -> int"""

    anterior = 1
    
    while numero >= 1:
        anterior = anterior * numero
        numero = numero - 1
    return anterior