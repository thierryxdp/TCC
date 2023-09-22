def lingua_p(palavra):
    """
    Função que recebe uma string e retorna essa
    string traduzida para a linguagem p
    
    str -- > str
    """
    
    palavra=palavra.lower()
    
    trad=''
    
    for letra in palavra:
        trad+=letra
        
        if letra not in 'bcdfghjklmnpqrstvwçxyz':
            trad+='p'+letra
    return trad