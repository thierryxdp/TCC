def freq_palavras(texto):
    '''
    Função recebe um texto e retorna um dicionário no qual cada palavra
    do texto assume o lugar de chave e quantidade de vezes que as mesmas
    aparecem assumem a posição dos valores.

    str -> dic
    '''
    
    partido = str.split(texto)
    dicionario_final = {}

    for i in range(0,len(partido)):
        
        part = partido[i]
        contando_palavras = list.count(partido, partido[i])
        dicionario_final[part] = contando_palavras
        
    return dicionario_final