def substitui(s, x, i):
    nova_string=s[0:i]+ x +s[i:]  
    #adiciona os elementos de s(da posição inicial 0 até a anterior a i) na variavel nova_string, adiciona o caracter x e depois adiciona o resto dos elementos de s.
    return nova_string