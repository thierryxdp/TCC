def inverte(palavra):
    if re.match(r'^\w+$', palavra):
    return palavra[::-1]
    return palavra