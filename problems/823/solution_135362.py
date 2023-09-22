def faltante(lista):
    """Lista que retorna o número da peça que falta em um quebra cabeça com N peças ordenadas em ordem crescente."""
    """lista->int"""
    x=0
    i=0
    while i<len(lista):
        x=x+lista[i]
        i=i+1
    return (((len(lista)+1)*(len(lista)+2))/2)-x