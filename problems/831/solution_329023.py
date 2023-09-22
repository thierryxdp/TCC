def lingua_p(palavra):
    """Passa todas palavra para minúscula usando a função lower,
    após isso verifica para cada letra da palavra se a mesma é vogal
    (contemplando todas as possibilidades de acentuação em português),
    caso a letra seja vogal, é a dicionada a mesma letra um p e a própria
    letra (ou seja letra se torna letra+'p'+letra), caso não seja vogal se
    mantém igual. Após isso, cada letra que passa pelo processo é adicionada
    a uma string inicialmente vazia, formando a palavra traduzida para a
    língua do p, onde consoantes se mantém iguais na palavra e a vogal passa
    pelo processo de mudança. Após todas as letras serem verificadas,
    retorna a palavra traduzida.
    str-> str"""
    palavra=palavra.lower()
    palavra_p=""
    for letra in palavra:
        if letra in 'aeiouáéíóúàâêôãõ':
            letra+="p"+letra
        palavra_p+=letra
    return palavra_p