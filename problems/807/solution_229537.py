def conta_frases(sti):
    """Função que retorna a quantidade de frases dentro da string parâmetro.
"""
    qua= sti.count('!')+sti.count('?')+sti.count('.')+sti.count('...')
    return sti.count('...')