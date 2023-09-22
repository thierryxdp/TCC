def uppCons(frase):
    i = 0
    uppFrase = ''
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            uppFrase = uppFrase + frase[i].upper()
            i = i + 1
       	else:
            uppFrase = uppFrase + frase[i]
   		return uppFrase