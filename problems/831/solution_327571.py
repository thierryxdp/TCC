def lingua_p(palavra):
    p=''.join('p'+palavra[i]+'p' if vogal in 'aeiouAEIOU' else vogal for vogal in palavra)
    return p