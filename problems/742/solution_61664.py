#Função recebe uma string s, um caractere x e um numero i
#Retorna uma string igual a s, exceto o elemento da posição i
def substitui(s,x,i):
    """Funçao que retorna uma string igual a s, e o elemento da posicao i vire o caractere x.
    string, int, int - > string"""
    return s[0:i]+str(x)+s[i+1:]