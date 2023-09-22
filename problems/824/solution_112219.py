def auxilio(frase):
    
    nova_frase = frase
    vogal = ['a', 'e', 'i', 'o', 'u', 'ã', 'ó', 'é', 'í', 'ú']
    posicao = []
    
    for i in nova_frase:
        if i not in vogal:
            list.append(i, posicao)
            #nova_frase = nova_frase.replace(i, str.upper(i))
  
    return posicao

#def uppCons(frase):
 #   
  #  final = list.map(auxilio, frase)
    
   # return final