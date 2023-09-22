def freq_palavras(frases):
    '''Retorna dicionário que cada palavra é chave
    com valor nºvezes que aparece
    str->dict'''
    
    Dicionario={}
    Palavras=str.split(frases)
    
    for PalavraEmSi in Palavras:
        VezesPalavra=list.count(Palavras,PalavraEmSi)
        Dicionario[PalavraEmSi]=VezesPalavra
        
    return Dicionario