def substitui(s,x,i)
    """"retorna uma string s substituindo o caractere da posição por x
    str,int,int->str"""
    novastring = s[0:i] + str(x) + s[i+1:]
    return novastring