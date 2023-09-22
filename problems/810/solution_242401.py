def inverte (frase:str) -> str:
    "recebe uma frase e inverte ela tirando todas as pontuações e letras maiusculas"
    
    pontuacoes = ['.', '!', '?', '-', ',', ';', ':', '...']
    
    #fazendo uma copia da frase original
    fraseAlterada = frase
    
    #substituindo cada pontuacao por espaço
    fraseAlterada = fraseAlterada.replace('.', ' ')
    fraseAlterada = fraseAlterada.replace('!', ' ')
    fraseAlterada = fraseAlterada.replace('?', ' ')
    fraseAlterada = fraseAlterada.replace('-', ' ')
    fraseAlterada = fraseAlterada.replace(',', ' ')
    fraseAlterada = fraseAlterada.replace(';', ' ')
    fraseAlterada = fraseAlterada.replace(':', ' ')
    fraseAlterada = fraseAlterada.replace('...', ' ')
    
    fraseMin = str.lower(fraseAlterada)
    
    fraseMin[::-1]
    
    return fraseMin