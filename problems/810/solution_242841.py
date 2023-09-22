def retira_pontuacao(frase):
    '''Calcular uma funcao que receba uma frase e retorne ela substituindo as pontuacoes por espaco;
    str -> str'''
    
    caractere1 = str.replace(frase, '-', ' ')
    caractere2 = str.replace(caractere1, ',', ' ')
    caractere3 = str.replace(caractere2, ':', ' ')
    caractere4 = str.replace(caractere3, ';', ' ')
    caractere5 = str.replace(caractere4, '.', ' ')
    caractere6 = str.replace(caractere5, '!', ' ')
    caractere7 = str.replace(caractere6, '?', ' ')
    
    ponto0 = caractere7

def inverte(frase):
    '''Calcular uma funcao que dada uma frase retorne ela inversa, em letra minuscula e sem pontuacao;
    str -> list'''
    
    frase1 = str.lower(ponto0)
    frase2 = str.split(frase1)
   
    return ''.join(frase2[::-1])