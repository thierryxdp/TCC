def hashtag(s):
    
    """Funçao que recebe uma string e insere 
    um '#' no inicio, meio e no final dela"""
    
    str1 = "#" + str1[:len(str1)//2] + "#" + str1[len(str1)//2:] + "#"
    
    return s