def hashtag(s):
    """recebe uma string e insere "#" no inicio, meio e no final dela. 
    str->str"""
    
    meio= len(s)//2
    return "#"+s[:meio]+"#"+s[meio:]+"#"a