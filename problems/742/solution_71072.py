def substitui(s,x,i):
  #Função que recebe uma string s, caractere x e um número inteiro i, e retorna uma string igual a s, substituindo o elemento da posição i pelo caractere x
  #str, str, int -> str
  if 0 <= i < len(s):
    return s.replace(s[i],x,1)