def hashtag(string):
    
    tamanho_da_string = len(string)
    
    if tamanho_da_string % 2 == 0:
        
        metade = int(tamanho_da_string/2)
    
        string_hashtag = "#" + string[:metade] + "#" + string[metade:] + "#"
        
        return string_hashtag
        
    else:
        
        metade_anterior = int(tamanho_da_string/2 - 0.5)
        
        string_hashtag = "#" + string[:metade_anterior] + "#" + string[metade_anterior:] + "#"
        
        return string_hashtag