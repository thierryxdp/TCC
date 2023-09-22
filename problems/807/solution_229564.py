def conta_frases(sti):
    """Função que retorna a quantidade de frases em uma dada string.
assinatura: str -> int
"""
    fra= str.replace(sti,'...','1')
    qua= fra.count('.')+fra.count('1')+fra.count('?')+fra.count('!')
    return qua