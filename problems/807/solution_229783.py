def conta_frases(texto):
    '''
       Dado um texto a função retorna quantas frases estão
       presentes nesse texto baseado nos pontos de conclusão
       no final de cada frase
       str -> int
    '''
    final = len(str.split'.'))
    exclamacao = len(str.split'!'))
    interrogacao = len(str.split'?'))
    reticencias = len(str.split '...'))
    return final + exclamacao + interrogacao + reticencias