def linagua_p(palavra):
    '''Função que recebe uma palavra (em português) e retorna esta mesma palavra
traduzida para a língua do P. Uma palavra foi traduzida para a lígua do P quando,
após cada vogal da palavra original, é inserida a sequência de letras p mais a
vogal original.
    str -> str
    '''
    palavra = str.lower(palavra)
    if 'a' in palavra:
        palavra = str.replace(palavra,'a','apa')
    if 'e' in palavra:
        palavra = str.replace(palavra,'e','epe')
    if 'i' in palavra:
        palavra = str.replace(palavra,'i','ipi')
    if 'o' in palavra:
        palavra = str.replace(palavra,'o','opo')
    if 'u' in palavra:
        palavra = str.replace(palavra,'u','upu')
    if 'ã' in palavra:
        palavra = str.replace(palavra,'ã','ãpã')
    if 'é' in palavra:
        palavra = str.replace(palavra,'é','apa')
    if 'õ' in palavra:
        palavra = str.replace(palavra,'õ','õpõ')
    if 'í' in palavra:
        palavra = str.replace(palavra,'í','ípí')
    if 'ó' in palavra:
        palavra = str.replace(palavra,'ó','ópó')
    if 'á' in palavra:
        palavra = str.replace(palavra,'á','ápá')
    return palavra