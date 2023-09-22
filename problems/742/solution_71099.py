def substitui(s,x,i):
  #Função que recebe uma string s, caracter x e um número inteiro i, e retorna uma string igual a s, substituindo o elemento da posição i pelo caracter x
  #str, str, int -> str
  if 0 <= i < len(s):
    return s[:i] + x + s[i+1:]
    #Somente substituir uma vez, na ocorrência de posição igual ao índice especificado