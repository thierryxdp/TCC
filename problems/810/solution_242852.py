def inverte(frase):
    '''Calcular uma funcao que dada uma frase retorne ela inversa, em letra minuscula e sem pontuacao;
    str -> list'''
    
    caractere1 = str.replace(frase, '-', ' ')
    caractere2 = str.replace(caractere1, ',', ' ')
    caractere3 = str.replace(caractere2, ':', ' ')
    caractere4 = str.replace(caractere3, ';', ' ')
    caractere5 = str.replace(caractere4, '.', ' ')
    caractere6 = str.replace(caractere5, '!', ' ')
    caractere7 = str.replace(caractere6, '?', ' ')
    caractere7 = sem_ponto
    
    Lminucula = str.lower(sem_ponto)
    
    split = str.split(Lminuscula)
   
    return ' '.join(split[::-1])