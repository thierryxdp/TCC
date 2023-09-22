def freq_palavras (frases):
    '''
       Função que recebe uma frase (frases) e retorna um
       dicionário onde cada palavra da frase é uma chave
       com o valor igual ao numero de vezes que a palavra
       aparece
       str -> dict
    '''
    dic={}
    lista=str.split(frase, ' ')
    while ' ' in lista == True:
        lista=lista.remove(' ')
    for palavra in frases:
        valor=lista.count(palavra) 
        dic.update({palavra:valor})