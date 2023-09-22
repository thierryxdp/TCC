def retira_pontuacao (frase:str)-> str:
    '''dada uma frase, retorna a frase, porém com pontuação substituída por
    espaço'''
    frase= str.replace (frase, '-', ' ')
    frase= str.replace (frase, ',', ' ')
    frase= str.replace (frase, ':', ' ')
    frase= str.replace (frase, ';', ' ')
    frase= str.replace (frase, '...', ' ')
    frase= str.replace (frase, '.', ' ')
    frase= str.replace (frase, '?', ' ')
    frase= str.replace (frase, '!', ' ')
    return frase