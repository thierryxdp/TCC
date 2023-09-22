def lingua_p(palavra_PT):
    """A função recebe uma string contendo uma palavra
    em português e retorna outra string com a palavra traduzida
    para a "língua do p" (após cada vogal, adiciona-se p + vogal)."""
    for letra in palavra_PT:
        if letra in 'aeiou':
            palavra_PT.replace(letra, 'p' + letra)
    return palavra_PT