# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    #if i+1>len(s) or i<-(len(s)):
        #print('i não pode ser maior que o comprimento da string')
    #else:
        inicio = s[:i]
        fim = s[i+1:]
        novoS = inicio+x+fim
        return novoS