def conta_frases(sti):
    """Função que retorna a quantidade de frases dentro da string parâmetro.
"""
    qua= 0
    if sti.split('.'):
        qua=+1
    if sti.split('!'):
        qua=+1
    if sti.split('?'):
        qua=+1
    if sti.split('...'):
        qua=+1
    return sti.split('.')