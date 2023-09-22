def inverte(frase):
    final = frase.replace(',', ' ')
    final1 = final.split(' ')
    final2 = final1[::-1]
    return final2