def lingua_P(palavra):
    '''Funcao que dada uma palavra (em português), traduz ela para a lingua do P.
Essa lingua funciona da maneira de que toda vogal é seguida da letra P, tendo como
exemplo o nome 'Gilson', que traduzido para a lingua do P fica 'gipilsopon'. A funcao
retorna a palavra inteira em caixa baixa, independente do tamanho inicial.
    str - > str'''
    palavra = palavra.lower()
    consoantes = 'bcdfghjklmnpqrstvwxyzç'
    vogais = 'a,ã,á,â,e,é,ê,i,í,î,o,õ,ó,ô,u,ú,û'
    TraducaoLinguaP = ''
    
    for letra in palavra:
        if letra in consoantes:
            TraducaoLinguaP += letra
        if letra in vogais:
            TraducaoLinguaP += letra + 'p' + letra
            
    return TraducaoLinguaP