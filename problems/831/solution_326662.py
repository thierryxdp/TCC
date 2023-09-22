def lingua_p(palavra):
    """Dada uma palavra, retorna a palavra na lingua do P, que significa que a cada vogal que aparece, é inserida a letra P+ a vogal que apareceu"""
    """entrada: str
    saida:str"""
    
    palavra1 = ""
    pos = 0
    
    while pos < len(palavra):
        if palavra[pos] in "aeiouAEIOU":
            palavra1 = palavra1 + palavra[pos] + "p" + palavra[pos]
            pos = pos +1
        
        elif palavra[pos] not in "aeiouAEIOU":
            palavra1 = palavra1 + palavra[pos]
            pos = pos +1
            
    return palavra1