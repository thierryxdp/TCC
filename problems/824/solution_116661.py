def uppCons(frase):
    '''Função que recebe uma frase e retorna a frase com todas
    as suas consoantes em maiúsculo. ent--> str  saida--> str'''
    
    indice = 0
    frase2 = frase.split('')
    
    while indice <= len(frase2):
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            newletra = str.upper(frase[indice])
        	list.insert(frase2,indice,newletra)
        	frase3 = ''.join(frase2)
  		indice=indice+1
    return frase3