def lingua_p(palavra):
    palavra_nova = str()
    
    for letra not in str.lower(palavra):
        palavra_nova += letra
        
    for letra in str.lower(palavra):
        palavra_nova += 'p'+str.lowre(palavra)+'p'
    
    return palavra_nova