def hashtag(s):
    
    """Função que recebe uma string e insere o caractere'#' no início, no meio e no final dela.
    
    Exemplo 1:
    
    Parâmetro:BOLA
    return:#BO#LA#
    
    Exemplo 2:
    
    Parâmetro:PORTA
    return:#PO#RTA#
    """
    return '#'s[0:len(s)//2]+'#'+s[len(s)//2:len(s)]'#'