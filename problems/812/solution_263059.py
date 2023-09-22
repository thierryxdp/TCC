def retira_pontuacao(frase):
    """Função que dada uma frase, retorna a frase onde
    todos os caracteres de pontuação (incluindo travessão,
    vírgula, além da pontuação de encerramento de frase)
    tenham sido substituídos por espaço."""
    frase1 = str.replace(frase, '!', '.')
    frase2 = str.replace(frase, '?', '.')
    frase3 = str.replace(frase, ';', '.')
    frase4 = str.replace(frase, '...', '.')
    frase5 = str.replace(frase, ',', '.')
    frase6 = str.replace(frase, ':', '.')
    return frase6