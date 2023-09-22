def substitui(s,x,i):
        """receber uma string s, uma caractere x e um numero inteiro entre 0 e o comprimento da string, e retorne uma string igual a s, exceto o elemento da posição i deve ser substituido pelo caractere x"""
        return s[0:i]+x+s[i+1:]