#Reutilizei o codigo da função que retira pontuação
#Em seguida criei uma nova para inverte a ordem das palavras
#O replace substitui uma frase especificada por outra frase especificada.
#O join pega todos os itens em um iterável e os une em uma string.

Uma string deve ser especificada como separador.
def retira_pontuacao(frase):
    """Dada uma frase pontuada, remove todos os pontos como travessao, virgula, dois pontos,
    e ponto final substituindo por espaço,
     str -> str"""
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    doispontos = virgula.replace(':', ' ')
    pontovirgula = doispontos.replace(';', ' ')
    pontofinal = pontovirgula.replace('.', ' ')
    pontointerrogacao = pontofinal.replace('?', ' ')
    pontoExclamacao = pontointerrogacao.replace('!', ' ')
    return pontoExclamacao

def inverte(frase):
    """A função remove as pontuações da frase, substitui as letras maisculas
    por minusculas e inverte a frase:
    str -> str"""
    frase = frase.replace('-', ' ')
    frase = frase.replace(',', '')
    frase = frase.replace(':', '')
    frase = frase.replace(';', '')
    frase = frase.replace('.', '')
    frase = frase.replace('?', '')
    frase = frase.replace('!', '')
    frase = str.lower(frase)
    frase = frase.split()
    frase = frase[::-1]
    frase = " ".join(frase)
    return frase