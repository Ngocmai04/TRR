def get_next_state(current_state, i, j, capacities):
    # lấy lượng nước trong bình i và j
    i_water, j_water = current_state[i], current_state[j]
    # thêm nước vào bình j cho đến khi đầy hoặc hết nước trong bình i
    amount = min(i_water, capacities[j] - j_water)
    next_state = list(current_state[:])
    next_state[i] -= amount
    next_state[j] += amount
    return tuple(next_state)


def pour_water(capacities, current_state, target, visited, path, algorithm):
    if current_state in visited:
        return False
    visited.add(current_state)
    path.append(current_state)

    if current_state[0] == target or current_state[1] == target:
        return True

    for i in range(3):
        for j in range(3):
            if i != j:
                next_state = get_next_state(current_state, i, j, capacities)
                if next_state and pour_water(capacities, next_state, target, visited, path, algorithm):
                    return True

    path.pop()
    return False


capacities = [10, 7, 4]
start_state = (0, 7, 4)
target = 2

visited = set()
path = []
pour_water(capacities, start_state, target, visited, path, algorithm='dfs')

if path:
    print("Found a solution:")
    for state in path:
        print(state)
else:
    print("No solution found.")
