"recebe uma string s, um inteiro i e um caractere x e retorna a string s e troca o elemente da posição de i pelo caractere x"
def substitui(s,x,i):
   meio = (s+x+i)
   return s[:0] + i[:len(meio)//2] + x[0:]