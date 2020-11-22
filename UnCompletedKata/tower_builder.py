def tower_builder(n_floors):

    my_list = []
    max = n_floors * 2 - 1
    upper = n_floors // 2 + 1
    lower = n_floors // 2
    space = " " * n_floors
    tower = "*" * n_floors
    for x in range(n_floors,0,-1):
        my_list.append(space[0:lower] + tower[lower:upper] + space[upper:n_floors])
        lower -= 1
        upper += 1
    return my_list

print(tower_builder(4))