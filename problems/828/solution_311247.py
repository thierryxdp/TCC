def primo(n):
    '''Função que verifica se um número é primo ou não
       int->boolean'''
    i=0
    lista=[]
    while i<=n:
        i=i+1
        if n%i==0:
            lista.append(i)
    if len(lista)>2:
        return "False"
    else:
        return "True"