def retira_pontuacao(txt):
    '''Dada uma frase txt, retorna a frase onde todos os 
    caracteres de pontuação (incluindo travessão, vírgula, 
    dois pontos, ponto e vírgula, além da pontuação de 
    encerramento de frase) tenham sido substituídos por 
    espaço
    str -> str'''
    pontos = '-,:;.!?'
    for ponto in pontos:
        txt = txt.replace(ponto,' ')
    return txt

def inverte(txt):
    '''Dada uma frase txt retorna suas palavras em 
    minusculas e em ordem invertida
    str = str'''
    txt = txt.lower()
    txt = retira_pontuacao(txt)
    txt = txt.split()
    txt = txt[::-1]
    return ' '.join(txt)