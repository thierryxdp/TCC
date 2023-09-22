def acima_da_media(lista):
    """Função retorna as notas dos alunas que obtiveram grau
    superior a média
    
    dados de entrada - > lista
    dados de saida .-> lista"""
    
    Q = len(lista)
    Soma = Sum(lista)
    Media = Soma/Q
    Maiores = maiores(lista,media)
    
    If media in maiores
    lista.remove(maiores,media)
    return Maiores