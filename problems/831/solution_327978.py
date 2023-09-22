def lingua_p(palavra):
    """ Função que recebe uma palavra como entrada 
        e retorna essa mesma palavra com múltiplas letras p
        str ---->str"""
    palavran=''
    
    for l in palavra:
        if l in "aáàeèéioóòuùúAEIOUÁÉÍÓÚ":
            palavran= palavran + l + 'p' + l
        else:
            palavran = palavran + l
            
    return palavran