def uppCons (frase:list) -> list:
    """Função que irá receber uma frase e irá retornar essa frase com todas as consoantes em letra maiúscula e as demais da forma como estavam.
    
    	Parameters:
        frase: frase que será alterada
        
        Returns:
        frase com as alterações feitas
    """
    
    posicao = 0
    frasefinal = frase
    while posicao < len(frase):
        if str.lower(frasefinal[posicao]) in 'bcdfghjklmnpqrstvwxyzç':
            frasefinal = str.replace(frasefinal, frasefinal[posicao], str.upper(frasefinal[posicao]))
        posicao = posicao + 1
    return frasefinal