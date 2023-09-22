def filtra_pares (a,b,c,d):
    """Calcula e retorna apenas os números pares da tupla origunal de entrada.
    tupla (int, int, int, int) -> tupla (int)"""
    if a % 2 ==0:
        mensagem1 = a
    else:
        mensagem1 = ''
    if b % 2 ==0:
        mensagem2 = b
    else:
        mensagem2 = ''
    if c % 2 ==0:
        mensagem3 = c
    else:
        mensagem3 = ''
    if d % 2 ==0:
        mensagem4 = d
    else:
        mensagem4 = ''
    return (mensagem1, mensagem2, mensagem3, mensagem4)