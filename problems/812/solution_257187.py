def chr_remove(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string

	print chr_remove(s, ",(.") # remove $,# e ( da string
string com caracteres.