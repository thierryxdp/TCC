def retira_pontuacao(frase):
    '''retorna a frase informada com todos os caracteres de pontuação substituidos por um espaço
    str -> str'''
    pontuacao = '-',',',':',';','.','!','?'
    
    if '-' in frase or ',' in frase or ':' in frase or ';' in frase or '.' in frase or '!' in frase or '?' in frase:
        return str.replace(frase,'pontuacao',' ')