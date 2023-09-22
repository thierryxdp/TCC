def uppCons(frase):
    """Função que, dada uma frase, retorna a frase com todas as suas consoantes em maiúsculas; str->str"""
    
    indice = 0
    retorno = ''
    
    while indice < len(frase):
        
        if str.lower(frase[indice]) in 'bcdfghjklmnpqrstvwxyz':
            retorno = retorno+str.upper(frase[indice])
            
            else:
                retorno = retorno+frase[indice]
                
    return retorno