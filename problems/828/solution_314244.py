def primo(num):
    '''Calcula e retorna se um número(num) passado como
       valor de entrada é primo ou não;
       int -> bool'''
    
    resposta = False
    pos = 0
    possiveis_num = list(range(2,num-1))
    
    while resposta == False and pos < num-2:
        
        if num % possiveis_num[pos] == 0:
            
            resposta = True
            
        pos += 1
        
    return resposta