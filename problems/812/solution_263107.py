def retira_pontuacao(frase):
    """Função que dada uma frase, retorna a frase onde
    todos os caracteres de pontuação (incluindo travessão,
    vírgula, além da pontuação de encerramento de frase)
    tenham sido substituídos por espaço."""
    str.strip(frase, '!')
    str.strip(frase, '?')
    str.strip(frase, ';')
    str.strip(frase, '...')
    str.strip(frase, ',')
    str.strip(frase, ':')
    str.strip(frase, '.')
    str.strip(frase, '-') 
    return frase