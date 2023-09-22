def substitui(s,x,i):
    '''Função que recebe uma string s, um caractere x e um número inteiro i e
    que retorna uma string s com o caractere x no lugar do elemento da posição i;
    str,str,int->str'''
    return s[0:i]+x+s[i+1:]