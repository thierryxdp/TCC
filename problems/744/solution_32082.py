def hashtag(s):
    
    """Funçao que recebe uma string e insere 
    um '#' no inicio, meio e no final dela"""
    
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    
    return s