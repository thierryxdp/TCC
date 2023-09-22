# A função recebe uma frase e retorna a mesma frase com todas as suas consoantes em letras
# maiúsculas e os demais caracteres exatamente como estavam na frase original
# string->string
#
def uppCons(frase):
    i=0
    nova_frase=frase
    while i < len(frase):
        if not frase[i] in 'AEIOUaeiouÁÀÃÉÍÓÕÚáàãéíóõú':
            u=str.upper(frase[i])
            nova_frase=str.replace(nova_frase,frase[i],u)
        i=i+1
    return nova_frase