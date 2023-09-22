def freq_palavras(frase):
    '''Função que recebe uma string e retorna um dicionário onde
    cada palavra dessa string seja uma chave e tenha como valor o
    número de vezes que a palavra aparece. 
    str->dict'''
    lista_str = str.split(frase)
    dicionario_resposta = {}
    for i in lista_str:
        vezes_aparece = lista_str.count(i)
        dicionario_resposta[i] = vezes_aparece
    return dicionario_resposta