def retira_pontuacao (frase:str) -> str:
    "recebe uma frase e substitui todos os caracteres por espaço"
    
    pontuacoes = ['.', '!', '?', '-', ',', ';', ':', '...']
    
    #fazendo uma copia da frase original
    fraseAlterada = frase
    
    #substituindo cada pontuacao por espaço
    fraseAlterada = fraseAlterada.replace(',', ' ')
    fraseAlterada = fraseAlterada.replace('!', ' ')
    fraseAlterada = fraseAlterada.replace('?', ' ')
    fraseAlterada = fraseAlterada.replace('-', ' ')
    fraseAlterada = fraseAlterada.replace(',', ' ')
    fraseAlterada = fraseAlterada.replace(';', ' ')
    fraseAlterada = fraseAlterada.replace(':', ' ')
    fraseAlterada = fraseAlterada.replace('...', ' ')
    return fraseAlterada