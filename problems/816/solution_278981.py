def maiores(num_list, n):
    old_list = []
    for i in range(len(num_list)):
        if i == 0:
            for j in range(len(num_list[0])):
                old_list.append(num_list[0][j])
        else:
            old_list.append(num_list[i])
    new_list = []
    for i in range(len(old_list)):
        if n < old_list[i]:
            new_list.append(old_list[i])
    return new_list