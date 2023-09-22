def freq_palavras(frases):
    '''
       funcao que recebe uma string e retorna
       um dicionario onde cada palavra dessa strinf seja uma 
       chave e tenha como valor o numero de vezes que a palavra aparece
       str
    '''
    palavras=frases.split()
    dic={}
    for caractere in palavras:
        cont= palavras.count(caractere)
        dic.update({caractere:cont})
    return dic# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis