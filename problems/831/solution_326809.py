def lingua_p(palavra):
    vowels = "AaEeIiOoUu"
    final=''
    for each in palavra:
        if each in vowels:
            final+=each+'p'+each
        else:
            final+=each
    return final