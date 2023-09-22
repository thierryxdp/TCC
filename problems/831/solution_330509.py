def lingua_p (palavra):
    """Função que recebe uma palavra e retorna esta mesma palavra trazudida para língua do P
    entrada: str
    saída: str"""
    palavra_minuscula=str.lower(palavra)
    palavra_final=''
    for letra in palavra_minuscula:
        if letra in 'aeiouáéíóúãõ':
            palavra_final=palavra_final+letra+'p'+letra
        else:
            palavra_final=palavra_final+letra
    return palavra_final