def repetidos(list):
    rep_num = 0
    i = 0
    while i < len(list):
        if i == 0:
            continue
        elif list[i] == list[i - 1]:
            rep_num += 1
        i += 1
    return rep_num