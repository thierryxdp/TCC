def retira_pontuacao(frase):
    '''substitui os caracteres de pontuação de uma frase por espaços'''
    n =>1 
    if n*'—' in frase:
        return frase.replace('—', ' ')
    else:
        if n*',' in frase:
            return frase.replace(',', ' ')
        else:
            if n*':' in frase:
                return frase.replace(':', ' ')
            else:
                if n*';' in frase:
                    return frase.replace(';', ' ')
                else:
                    if n*'.' in frase:
                        return frase.replace('.', ' ')
                    else:
                        if n*'?' in frase:
                            return frase.replace('?', ' ')
                        else:
                            if n*'!' in frase:
                                return frase.replace('!', ' ')