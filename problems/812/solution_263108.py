def retira_pontuacao(frase):
    """Função que dada uma frase, retorna a frase onde
    todos os caracteres de pontuação (incluindo travessão,
    vírgula, além da pontuação de encerramento de frase)
    tenham sido substituídos por espaço."""
    frase1 = str.strip(frase, '!')
    frase2 = str.strip(frase, '?')
    frase3 = str.strip(frase, ';')
    frase4 = str.strip(frase, '...')
    frase5 = str.strip(frase, ',')
    frase6 = str.strip(frase, ':')
    frase7 = str.strip(frase, '.')
    frase8 = str.strip(frase, '-') 
    return frase8