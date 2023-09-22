def retira_pontuacao(frase):
    '''Função que retorna uma frase espaçando todos os caracteres'''
    'str -> str'
    frase==str
    #-->('!',',','.',';','?','!','-')

    if  '!' or ',' or '.' or ';' or '?' or '!' or '-' in frase:
        return frase.replace('!',' ').replace(',',' ').replace('.',' ').replace(';',' ').replace('?',' ').replace('!',' ').replace('-',' ')