import random

# Generate random cylinder requests
requests = [random.randint(0, 4999) for _ in range(1000)]

# Write requests to a file
with open('cylinder_requests.txt', 'w') as file:
    for request in requests:
        file.write(str(request) + '\n')
