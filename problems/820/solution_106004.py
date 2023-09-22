def posLetra(fr, lt, n): 
    '''Função que recebe como entrada uma string, uma letra e um número que indica a
ocorrência desejada da letra, e retorna a posição da string que aquela ocorrência
da letra está. Caso exista menos ocorrências do que a ocorrência pedida, a função
deve retornar -1.
Assinatura: tuple (str, str, int) -> int
Casos de teste:
'''
    if str.count(fr, lt) < n: 
        return -1
    else:
        return fr.index(lt)