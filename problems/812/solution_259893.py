def retira_pontuacao(fraseAlterada):
    """ dado uma frase retorna a mesma com todas as pontuações substituidas por espaço
    str->str"""
    fraseAlterada = fraseAlterada.replace('...',' ')
        fraseAlterada = fraseAlterada.replace('.',' ')
        fraseAlterada = fraseAlterada.replace(',',' ')
        fraseAlterada = fraseAlterada.replace('-',' ')
        fraseAlterada = fraseAlterada.replace(';',' ')
        fraseAlterada = fraseAlterada.replace(':',' ')
        fraseAlterada = fraseAlterada.replace('?',' ')
        fraseAlterada = fraseAlterada.replace('!',' ')
        return fraseAlterada