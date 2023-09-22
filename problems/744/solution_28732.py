def hashtag(s):
    ''' Função que dada uma string qualquer (s) retorna o 
    caractere # no início,  no meio e no final dessa string
    Entrada: str
    Retorno: str '''
    
    string_par = "#"+s[:len(s)//2]+"#"+s[len(s)//2:]+"#"
    string_impar = "#"s[:len(s)//2]+"#"+s[len(s)//2:]+"#"
    
    if len(s)%2==0:
        return string_par
    
    else:
        return string_impar