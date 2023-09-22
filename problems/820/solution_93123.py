def posLetra(frase,letra,n):
    '''Função que dada uma frase, uma letra, e uma ocorrência n da letra, retorna a posição desta letra na frase na enésima ocorrência.
    Caso exista menos ocorrências do que a informada, a função retorna o valor -1
    str, str, int -> int'''
    i=0
    inicio=0
    while i<n:
        inicio+=str.find(frase,letra,inicio)-inicio+1
        i+=1
    return inicio-1