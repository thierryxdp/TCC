def auxilio(frase):
    
    
    str.split(frase)
    vogal = ['a', 'e', 'i', 'o', 'u']
    
    for i in frase:
        if i in vogal:
            return "Hello"
            
    lista = str.join('',frase)
    
    return lista