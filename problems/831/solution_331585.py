def lingua_p(palavra_PT):
    """A função recebe uma string contendo uma palavra
    em português e retorna outra string com a palavra traduzida
    para a "língua do p" (após cada vogal, adiciona-se p + vogal)."""
    palavra_P = ''
    for letra in palavra_PT:
        if letra not in 'aeiouáéíóúãõâêô':
            palavra_P += letra
        else:
            palavra_P += letra + 'p' + letra
    return palavra_P