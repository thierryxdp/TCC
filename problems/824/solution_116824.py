def uppCons(frase):
    '''funcao que recebe uma frase e retorna todas as consoantes
       minusculas em maiusculas
       str -> str'''
    i = 0
    palavra = ''
    'QWRTÇYPSDFGHJKLZXCVBNMqwrtyçpsdfghjklzxcvbnm'
    while i < len(frase):
        nova_frase = frase[i]
        if nova_frase in 'QWRTÇYPSDFGHJKLZXCVBNMqwrtyçpsdfghjklzxcvbnm':
            nova_frase = nova_frase.upper()
        palavra += nova_frase
        i += 1
    return palavra