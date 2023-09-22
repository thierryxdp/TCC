# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista,valor):
    soma=[]
    for i in range(0,len(lista)):
        if lista[i] in produtos:
            soma.append(produtos[lista[i]])
        	i=i+1
    return round(sum(soma),2)