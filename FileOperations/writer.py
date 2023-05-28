def remove_row_by_name(filename, player_name):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if player_name in line:
            del lines[i]
            break

    with open(filename, 'w') as file:
        file.writelines(lines)

    print(f"Player '{player_name}' removed {filename}.")

def add_row(filename,data):
    print(filename)
    with open(filename, 'a') as file:
        file.write(data+'\n')
