def substitui(s,x,i):
        """Função que faz insere x numa posição da string"""
    #s = string | x = caractere qualquer | i = um inteiro entre 0 e o comprimento da string
    #string, int, int -> string
      return s[:i]+x+s[i+1:]