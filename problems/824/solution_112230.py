def auxilio(frase):
    
    nova_frase = frase
    vogal = ['a', 'e', 'i', 'o', 'u', 'ã', 'ó', 'é', 'í', 'ú', ' ']
    letra_mod = []
    u = 0
    posicao = []
    
    
    for i in nova_frase:
        if i not in vogal:
            nova_frase = nova_frase.replace(i, str.upper(i))
    
    
  
    return nova_frase

def uppCons(frase):
    
    lista = list(map(auxilio, frase))
    final = str.join('', lista)
    
    return final