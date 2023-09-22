def posLetra(texto,letra,ocorrencia):
    
    ''' Recebe como entrada uma string, uma letra e um numero, que indica qual 
    ocorrencia daquela letra (na ordem que aparece no texto) se deseja. A 
    funcao retorna o indice de aparicao da string daquela ocorrencia da letra.
    Caso haja menos ocorrencias da letra do que a que foi pedida, eh retornado 
    o numero -1;
    
    Exemplo: 
        texto = 'Gabriela gosta de paçoca.'
        letra = 'o'
        ocorrencia = 2
        
        retorno: 21 
        (o indice da segunda ocorrencia da letra 'o') 
        
    str, str, int -> int '''
   
    aparicao = 1   # primeira aparicao da letra no texto 
    total_aparicoes = str.count(texto,letra)
    inicioBusca = str.find(texto,letra) # iniciar a busca da posicao na primeira ocorrencia
    
    if total_aparicoes < ocorrencia: 
        
        return -1
    
    while aparicao <= ocorrencia:  # enquanto a aparicao analisada <= a desejada
        
            posicao = str.find(texto,letra,inicioBusca)
            
            aparicao = aparicao + 1 # proxima aparicao 
            inicioBusca = posicao + 1 # iniciar a busca no elemento seguinte da aparicao analisada
        
    return posicao