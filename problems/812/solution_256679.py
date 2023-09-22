def retira_pontuacao(frase):
    '''substitui os caracteres de pontuação de uma frase por espaços'''
    if '—' in frase:
        return frase.replace('—', ' ')
    else:
        if ',' in frase:
            return frase.replace(',',' ')
        else:
            if ':' in frase:
                return frase.replace(':', ' ')
            else:
                if ';' in frase:
                    return frase.replace(';', ' ')
                else:
                    if '.' in frase:
                        return frase.replace('.', ' ')
                    else:
                        if '?' in frase:
                            return frase.replace('?', ' ')
                        else:
                            if '!' in frase:
                                return frase.replace('!', ' ')