def uppCons(frase):
    
    nova_frase = frase
    str.split(nova_frase)
    vogal = ['a', 'e', 'i', 'o', 'u']
    i = 0
    
    while i < len(nova_frase):
        if i not in vogal:
            nova_frase.upper(i)
        i = i+1
        
    return a