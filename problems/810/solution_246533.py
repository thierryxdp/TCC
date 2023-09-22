def retira_pontuacao(frase):
    """Função que dada uma frase, retorna a frase onde
    todos os caracteres de pontuação (incluindo travessão,
    vírgula, além da pontuação de encerramento de frase)
    tenham sido substituídos por espaço."""
    frase1 = str.replace(frase, '!', ' ')
    frase2 = str.replace(frase1, '?', ' ')
    frase3 = str.replace(frase2, ';', ' ')
    frase4 = str.replace(frase3, '...', ' ')
    frase5 = str.replace(frase4, ',', ' ')
    frase6 = str.replace(frase5, ':', ' ')
    frase7 = str.replace(frase6, '.', ' ')
    frase8 = str.replace(frase7, '-', ' ') 
    return frase8

def inverte(frase):
    """"""
    frase1 = retira_pontuacao(frase)
    frase2 = str.lower(frase1)
    lista = str.split(frase2)
    lista1 = list.reverse(lista)
    return lista1