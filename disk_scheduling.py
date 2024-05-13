import sys


def fcfs(requests, initial_position):
    total_head_movements = 0
    current_position = initial_position
    for request in requests:
        total_head_movements += abs(request - current_position)
        current_position = request
    return total_head_movements


def scan(requests, initial_position, total_cylinders):
    requests.sort()
    total_head_movements = 0
    current_position = initial_position
    head_direction = -1  # Initially, move towards lower cylinders
    while requests:
        if current_position in requests:
            requests.remove(current_position)
        if current_position == 0 or current_position == total_cylinders - 1:
            head_direction *= -1
        current_position += head_direction
        total_head_movements += 1
    return total_head_movements


def c_scan(requests, initial_position, total_cylinders):
    requests.sort()
    total_head_movements = 0
    current_position = initial_position
    while requests:
        if current_position in requests:
            requests.remove(current_position)
        if current_position == total_cylinders - 1:
            current_position = 0
        else:
            current_position += 1
        total_head_movements += 1
    return total_head_movements


def main():
    if len(sys.argv) != 3:
        print("Usage: python disk_scheduling.py [initial_position] [file_name]")
        return

    initial_position = int(sys.argv[1])
    file_name = sys.argv[2]

    try:
        with open(file_name, 'r') as file:
            requests = [int(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        print("File not found.")
        return

    total_cylinders = 5000

    # Task 1
    print("Task 1:")
    print("FCFS Head Movements:", fcfs(requests.copy(), initial_position))
    print("SCAN Head Movements:", scan(requests.copy(), initial_position, total_cylinders))
    print("C-SCAN Head Movements:", c_scan(requests.copy(), initial_position, total_cylinders))

    # Task 2
    print("\nTask 2:")
    print("FCFS Head Movements:", fcfs(sorted(set(requests)), initial_position))
    print("SCAN Head Movements:", scan(sorted(set(requests)), initial_position, total_cylinders))
    print("C-SCAN Head Movements:", c_scan(sorted(set(requests)), initial_position, total_cylinders))


if __name__ == "__main__":
    main()
