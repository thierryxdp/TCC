def uppCons(frase):
    '''Função que recebe uma frase e retorna a frase com todas
    as suas consoantes em maiúsculo. ent--> str  saida--> str'''
    
    indice = 0
    resposta = ''
    
    
    while i <= len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            newfrase = str.upper(frase[indice])
     	indice = indice + 1
  	return newfrase