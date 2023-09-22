def inverte(frase):
    '''Função que recebe uma frase e retorna essa frase com as palavras na ordem inversa;
    str -> str'''
    pontuacao = ['—','-',',',':',';','.','!','?']
    sem_pontuacao = ''
    palavras = str.split(frase)
    ordem_inversa = palavras[::-1]
    nova_frase = str.join(" ",ordem_inversa)
    
    for i in nova_frase:
        if i not in pontuacao:
            sem_pontuacao += i
        else:
            sem_pontuacao += ''
            
    return sem_pontuacao.lower()