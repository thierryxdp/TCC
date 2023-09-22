# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    
    """ Recebe uma string s, um numero inteiro i entre 0 e o comprimento 
    da string e um caracter x. Retorna uma string igual a s porem o caracter 
    da posicao i, sera substituido por x"""
    
    Largura = len(s)

    
    if i >= 0 and i <= Largura:
        
        S = list(s)
        S[i] = str(x)
        s = "".join(S)
        
        
        
        
        return s