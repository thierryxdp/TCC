def auxilio(frase):
    """Função auxiliar que recebe como entrada uma frase e retorna a mesma com todas as 
	consoantes em maiúscula.
    str -> str"""
    
    
    nova_frase = frase
    vogal = ['a', 'e', 'i', 'o', 'u', 'ã', 'ó', 'é', 'í', 'ú', ' '] 
    
    for i in nova_frase:
        if i not in vogal:
            nova_frase = nova_frase.replace(i, str.upper(i))
  
    return nova_frase

def uppCons(frase):
    """Função que, dada uma frase, retorna todas suas consoantes
    em letra maiúscula.
    str -> str"""
    
    lista = list(map(auxilio, frase))
    final = str.join('', lista)
    
    return final