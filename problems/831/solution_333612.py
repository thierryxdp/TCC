import itertools
def p_encode(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    s_groups = [(k, list(v)) for k, v in itertools.groupby(s, lambda c: c.lower() in vowels)]
    p_output = []

    for is_vowel_group, group_chars in s_groups:
        p_output.extend(group_chars)
        if is_vowel_group:
            p_output.append("p")
            p_output.extend(c.lower() for c in group_chars)

    return "".join(p_output)