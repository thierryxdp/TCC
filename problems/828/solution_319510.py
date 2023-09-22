def primo(n):
    i=1
    saida=[]
    while i<=n:
        if n%i==0:
            saida.append(str(i))
        i=i+1
    if saida=[]:
		return "É primo"
    else:
        return "Não é primo"