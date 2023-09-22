def quant_palavras(frase):
    ''' Dada uma frase como entrada (entre aspas simples ou duplas), a funcao 
    retorna a quantidade de palavras que ela possui; 
    string -> int '''
    
    frase1 = str.strip(frase)
    frase2 = frase1.replace(' ','*')
    
    return len(str.split(frase2,'*'))