def freq_palavras(frases):
    '''
       Função que recebe uma frase (frases) e retorna um
       dicionário onde cada palavra da frase é uma chave
       com o valor igual ao numero de vezes que a palavra
       aparece
       str -> dict
    '''
    frases=str.lower(frases)
    #apagando os pontos
    remover=['?','.',',','!']
    for pontos in remover:
        frases=str.replace(frases,pontos,'')
    #lista com palavras
    lista=frases.split(' ')
    #formando dicionario
    dic={}
    for palavra in lista:
        valor=lista.count(palavra) 
        dic.update({palavra:valor})
    return dic
# Escolha nomes elucidativos para suas variáveis