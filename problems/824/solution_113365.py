def uppCons(frase):
    ''''''
    maiuscula= str.upper(frase)
    
    while 'AEIOU' in maiuscula:
        str.replace('AEIOU','aeiou')
        
    return maiuscula