def substitui(s,x,i):
#Função que recebe como entrada uma string 's', um caractere 'x' e um numero inteiro 'i' entre
#zero e o comprimento da string 's'. Retornando a mesma string, mas com o caractere 'x' no lugar do caractere 
#que se encontrava no lugar 'i'.
#entrada: string, string e int.
#saida: string
    return s[0:i]+x+s[i+1:]