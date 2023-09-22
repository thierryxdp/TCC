def auxilio(frase):
    
    nova_frase = frase
    vogal = ['a', 'e', 'i', 'o', 'u', 'ã', 'ó', 'é', 'í', 'ú']
    
    for i in nova_frase:
        if i not in vogal:
            nova_frase = nova_frase.replace(i, str.upper(i))
  
    return nova_frase

def uppCons(frase):
    
    final = map(auxilio, frase)
    
    return final