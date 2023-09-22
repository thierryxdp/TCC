def altera_frase(frase,palavra,posicao):
    """Função que recebe um determinada frase, palavra e posição
e, caso essa palavra ja exista na frase, retorna a frase, transformando
a primeira aparição dessa palavra em maiúscula. Caso ela não exista na
frase ainda, ela sera adicionada na posição indicada; Entrada: String,string e int
Saída:string"""
    frase1=frase.split()

    if palavra in frase1:
        splitada=frase.split()
        x=list.index(splitada,palavra)
        maiuscula=palavra.upper()
        W=splitada[x]=maiuscula
        H=" ".join(splitada)
        return H
    else:
        splitada2=frase.split()
        z=palavra.split()
        w="".join(z)
        splitada2[posicao:posicao]=z
        J=" ".join(splitada2)
        return J