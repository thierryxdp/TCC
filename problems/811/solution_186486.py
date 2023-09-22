if _name_ == '_main_':
    mattress_dimen = sorted([int(x) for x in input().split()])
    door_dimen = sorted([int(x) for x in input().split()])

    if mattress_dimen[0] <= door_dimen[0] and mattress_dimen[1] <= door_dimen[1]:
        return('S')
    else:
        return('N')