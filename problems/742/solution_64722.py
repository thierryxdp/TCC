# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que recebe uma string, um caracter e um
    inteiro e retorna uma string 
    entrada: string, int, int 
    saida: string
    '''
    comprimentoStr: 0<i<len(s)
    substituidor: l=list(s)
    substituinte: l[i]=str(x)
    resultado: s="".join(l)
        return print(s)