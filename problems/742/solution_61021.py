'''Função que recebe uma string s, um caractere x e um número inteiro
   i entre 0 e o comprimento da string, e retorna uma string igual a s,
   porém com o elemento i substituído pelo caractere x.
   Os parâmetros s e x devem, obrigatoriamente, ser indicados entre aspas.
   tupla(str,str,float) -> str'''
def substitui(s,x,i):
    return s[:i]+x+s[(i+1):]