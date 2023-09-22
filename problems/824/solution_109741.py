def uppCons(frase):
    str.upper(frase)
    frasenova = ''
    i = 0 
    
    while i < len(frase):
        if frase[i] in 'AEIOU':
            frasenova += str.lower(frase[i])
        i += 1
   return frasenova