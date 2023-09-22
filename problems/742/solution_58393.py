# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """resulta em um substituição de uma letra da string inicial
    Parametros: 
    Entrada:string,string,int(entre 0 e o comprimento da string 's' 
    Saida:string"""
		if len(s)==i:
      			return s[0:i]+str(x)
   		else:
       			return s[0:i]+str(x)+s[i+1:]