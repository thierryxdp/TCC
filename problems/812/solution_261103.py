def retira_pontuacao(frase):
    '''Calcular uma funcao que receba uma frase e retorne ela substituindo as pontuacoes por espaco;
    str -> str'''
    
    caractere1 = str.replace(frase,'-','')
    caractere2 = str.replace(frase,',','')
    caractere3 = str.replace(frase,':','')
    caractere4 = str.replace(frase,';','')
    caractere5 = str.replace(frase,'.','')
    caractere6 = str.replace(frase,'!','')
    caractere7 = str.replace(frase,'?','')
    
    return caractere7