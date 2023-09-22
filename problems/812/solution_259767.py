def retira_pontuacao(frase:str)->str:
    pontuacoes = ['.','!','?','-',',',';',':','...']
    
    fraseAlterada = frase

    fraseAlterada = fraseAlterada.replace('...',' ')
    fraseAlterada = fraseAlterada.replace('.',' ')
    fraseAlterada = fraseAlterada.replace(',',' ')
    fraseAlterada = fraseAlterada.replace(';',' ')
    fraseAlterada = fraseAlterada.replace(':',' ')
    fraseAlterada = fraseAlterada.replace('-',' ')
    fraseAlterada = fraseAlterada.replace('!',' ')
    fraseAlterada = fraseAlterada.replace('?',' ')    
    
    return fraseAlterada