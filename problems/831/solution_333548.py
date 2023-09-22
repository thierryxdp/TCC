#Lingua do P
def lingua_p(palavra):
    #receba como parâmetro uma palavra (em português) e retorne esta mesma palavra traduzida: sring => string#
    d = 1
    palavra = palavra.lower()
    palavra_p = list(palavra)
    for i in range(0, len(palavra)):
        if((palavra[i] not in 'bcdfghjklmnpqrstvwxyz')):
            palavra_p.insert(i+d, 'p'+palavra[i
            d += 1
    palavra_p = ''.join(palavra_p
    return palavra_p