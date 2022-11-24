def victory(counter, step_list):
    if counter < 3:
        return False
    elif counter == 3:
        x_sum = set(map(lambda x: x[0], step_list))
        y_sum = set(map(lambda x: x[1], step_list))
        if (len(x_sum) == len(y_sum) and len(x_sum) == 3) or (
                len(x_sum) + len(y_sum) == 4 and (len(x_sum) == 1 or len(y_sum) == 1)
        ):
            return True
    else:
        return False

print(victory((3, [[(0, 0)], [(0, 1)], [(0, 2)]])))