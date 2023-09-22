def fatorial(numero):
    """Função que retorna o fatorial do numero; int->int  """
    i=1
    novo= numero
    while i<novo:
        numero= numero*i
        i+=1
    return numero