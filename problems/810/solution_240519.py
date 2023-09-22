def inverte(frase):
    final = frase.replace(',', ' ')
    final1 = final.str.split()
    final2 = final1.str.join[::-1]
    return final2