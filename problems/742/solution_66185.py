def substitui(s,x,i):
    "função que dadoas uam string s, uma caractere x e um int i..."
    "retorna uma uma str==s, exceto o elemento da posição i deve ser substituído pelo caractere x"
	if i == 0:
        return x+s[1:]
    if i == len(s):
        return s[0:lem(s)] + x
    if == meio:
        return s[0:i] + x + s[i+1:]