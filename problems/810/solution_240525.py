def inverte(frase):
    final = frase.replace(',', ' ')
    final1 = final.split(' ')
    final2 = reverse(final1)
    return final2