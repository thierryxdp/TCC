def lingua_p (frase):
    """Função que recebe uma frase e a retorna na língua do p, ou seja, após
    cada vogal é inserida a letra p e a vogal novamente. O frase retornada terá
    somente letras minusculas
    string->string"""
    traducao=""
    str.lower(frase)
    for letra in frase:
        if letra not in 'qwrtypsdfghjklzxcvbnm .,;:()!?':
            letra_p=letra+'p'+letra
            traducao=traducao+letra_p
        else:
            traducao=traducao+letra
    return traducao