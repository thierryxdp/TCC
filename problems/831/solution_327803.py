def lingua_p(palavra):
    palavra_nova = str()
    letra = 'aeiouéúáàíó'
    for str.lower(letra) not in str.lower(palavra):
        palavra_nova += letra
    for str.lower(letra) in str.lower(palavra):
        palavra_nova += 'p'+str.lowre(palavra)+'p'
    
    return palavra_nova