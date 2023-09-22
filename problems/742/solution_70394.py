def substitui(s,x,i):
    '''Função que retorna uma string igual a s,sendo que o elemento da 
    posição i é substituído pelo caractere x
   str, str, int -> str'''
   s[i]=x
   return str1[0:i] + x + str1[i + 1:]