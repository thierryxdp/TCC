def inverte(frase):
    frase1 = frase.replace('.', ' ')
    frase2 = frase1.replace('-', ' ')
    final = frase2.replace(',', ' ')
    final1 = final.split()
    final2 = final1[::-1]
    final3 = ' '.join(final2)
    return final3.lower()