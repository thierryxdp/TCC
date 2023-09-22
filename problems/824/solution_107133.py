def uppCons(s):
    s_nova = s.upper()
    if 'A' in s_nova:
        s_nova = s_nova.replace('A','a')
    elif 'E' in s_nova:
        s_nova = s_nova.replace('E','e')
    elif 'I' in s_nova:
        s_nova = s_nova.replace('I','i')
    elif 'O' in s_nova:
        s_nova = s_nova.replace('O','o')
    elif 'U' in s_nova:
        s_nova = s_nova.replace('U','u')
    return s_nova