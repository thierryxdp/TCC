def retira_pontuacao(frase):
    """ dado uma frase retorna a mesma com todas as pontuações substituidas por espaço
    str->str"""
    
        frase = fraseAlterada
        fraseAlterada = fraseAlterada.replace('...',' ')
        fraseAlterada = fraseAlterada.replace('.',' ')
        fraseAlterada = fraseAlterada.replace(',',' ')
        fraseAlterada = fraseAlterada.replace('-',' ')
        fraseAlterada = fraseAlterada.replace(';',' ')
        fraseAlterada = fraseAlterada.replace(':',' ')
        fraseAlterada = fraseAlterada.replace('?',' ')
        fraseAlterada = fraseAlterada.replace('!',' ')
        return fraseAlterada