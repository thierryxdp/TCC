def lingua_p(palavra):
    '''Função que recebe uma palavra e retorna
    a mesma traduzida para a lingua do P;
    entrada: str
    saída: str'''
    lingua = ''
    for letra in range(len(palavra)):
        if palavra[letra] in ('a','A','ã','Ã','â','Â','à','À','á','Á',
                              'e','E','É','é','Ê','ê','í','Í','Ó','ó'
                              ,'i','I','o','O','ô','Ô','õ','Õ',
                              'u','U','ú','Ú'):
            lingua += palavra[letra] + 'p' + palavra[letra]
        else:
            lingua += palavra[letra]
    return lingua.lower()