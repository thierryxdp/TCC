def uppCons(frase):
    
    """
    str---.str
    é criada uma string vazia e as letras antigas vão sendo adicionadas
    à string nova, de forma que as consoantes são colocadas na nova 
    string em maiúsculo pela funcao str.upper e as vogais são apenas
    colocadas de volta na funcao
    """
    
    i = 0
    
    l_novafrase=''
    
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            l_novafrase += str.upper(frase[i])
        else:
            l_novafrase += frase[i]
            
        i += 1
        
    return l_novafrase