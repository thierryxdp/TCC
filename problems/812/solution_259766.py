def retira_pontuacao(frase: str) -> str:
    '...'
    
    # Pontuacões
    pontuacoes = ['.', '!', '?', '-', ',', ';', ':', '...']
    
    # Fazendo uma cópia da frase original
    fraseAlterada = frase
    
    # Substituir cada pontuacao por espaço
    fraseAlterada = fraseAlterada.replace('...', ' ')    
    fraseAlterada = fraseAlterada.replace('.', ' ')
    fraseAlterada = fraseAlterada.replace(',', ' ')
    fraseAlterada = fraseAlterada.replace(';', ' ')
    fraseAlterada = fraseAlterada.replace(':', ' ')
    fraseAlterada = fraseAlterada.replace('-', ' ')
    fraseAlterada = fraseAlterada.replace('!', ' ')
    fraseAlterada = fraseAlterada.replace('?', ' ')
    
    # OU str.replace(fraseAlterada, ...)
    
    return fraseAlterada