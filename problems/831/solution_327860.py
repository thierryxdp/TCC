def lingua_p(palavra):
    """Funcao que converte a palavra inserida para a palavra da lingua do P;
    str -> str"""
    
    translate = ''
    
    for letra in palavra:    
        if letra in "aeiouAEIOUáéàóò":
            translate += letra + 'p' + letra
          
        else:
            translate+= letra
            
    return translate