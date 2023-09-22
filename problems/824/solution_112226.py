def uppCons(frase):
    
    nova_frase = frase
    vogal = ['a', 'e', 'i', 'o', 'u', 'ã', 'ó', 'é', 'í', 'ú', ' ']
    letra_mod = []
    u = 0
    posicao = []
    
    
    for i in nova_frase:
        if i not in vogal:
            list.append(letra_mod, i)
            u = u+1
            list.append(posicao, u)
            #nova_frase = nova_frase.replace(i, str.upper(i))
    
    
  
    return posicao

#def uppCons(frase):
 #   
  #  final = list.map(auxilio, frase)
    
   # return final