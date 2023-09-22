def uppCons(frase):
    i = 0
    palavra = ''
    'QWRTÇYPSDFGHJKLZXCVBNMqwrtyçpsdfghjklzxcvbnm'
    while i < len(frase):
        nova_frase = frase[i]
        if nova_frase in 'QWRTÇYPSDFGHJKLZXCVBNMqwrtyçpsdfghjklzxcvbnm':
            nova_frase.upper()
            palavra += nova_frase
        i += 1
    return palavra