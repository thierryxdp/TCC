def retira_pontuacao(frase):
    '''A função vai retirar qualquer tipo de pontuação que existe em um frase, como
    travessão, vírgula, dois pontos, ponto e virgula e ponto final e retornará a mesma frase com
    espaços no lugar das pontuações.
    
    dados de entrada -> string
    dados de saída -> string'''
    
    lista_retrita = ['-',',',':',';','.','!','?']
    
    x1 = '-' in frase
    x2 = ',' in frase
    x3 = ':' in frase
    x4 = ';' in frase
    x5 = '.' in frase 
    x6 = '!' in frase
    x7 = '?' in frase
    
    
    if :
        frase_nova = str.replace(frase,," ")
        return