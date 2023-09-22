# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):#ENTREGANDO TOTALMENTE FORA DO PRAZO, SÓ AGORA 
    #PUDE COMPREENDER A LÓGICA DE MANIPULAÇÃO DE VALORES IMUTAVEIS.
    #FEITO PARA FINS DE COMPREENSÃO.
    """
    Função que recebe uma string(s), um caractere(x) e um número
    inteiro(i) e retorne uma string igual s, mas que substitua o 
    caracter localizado no indice i da string(s) pelo caracter x.
    Paramêtro de Entrada: string, string, int
    Valor de Saida: string
    """
    string=''
    string= string+s[0:i]
    string= string+x
    string= string+s[i+1:]
    
    return string