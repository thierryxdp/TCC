def substitui(s,x,i):
    """Retorna a string que é o primeiro parâmetro de entrada, mas com o elemento da posiçao igual ao terceiro parâmetro substituido pelo segundo parâmetro;
    str,str,int->str"""
    return s[0:i]+x+s[i+1:]