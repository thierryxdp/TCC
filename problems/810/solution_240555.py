def inverte(frase):
    """Inverte a sua frase: str -> str"""
    frase1 = frase.replace('.', ' ')
    frase2 = frase1.replace('-', ' ')
    frase3 = frase2.replace('!', ' ')
    frase4 = frase3.replace('?', ' ')
    final = frase4.replace(',', ' ')
    final1 = final.split()
    final2 = final1[::-1]
    final3 = ' '.join(final2)
    return final3.lower()