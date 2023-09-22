def maiores(inteiros,n):
    '''A funcao recebe uma lista de inteiros e um numero n e retorna uma lista com
todos os numeros maiores do que n na lista de inteiros
list,int->list'''
    inteiros.append(n)
    inteiros.sort()
    lista=inteiros[inteiros.index(n)+1:]
    return lista

def acima_da_media(notas):
    '''A funcao recebe uma lista de notas de uma turma e retorna as notas que estao
acima da media geral da turma list->list'''
    n=(sum(notas)/len(notas))
    notasmaiores=maiores(notas,n)
    return notasmaiores