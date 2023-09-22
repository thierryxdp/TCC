def substitui(s,x,i):
    "a função retorna uma string igual a de entrada com excessão do elemento i que é substituido por x 
    string, int, int -> string"
    return s[0:i]+x+s[i+1::1]