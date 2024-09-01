with open('zen.txt', 'r', encoding='utf-8') as file:
    zen = file.readlines()

# for i in range(len(zen)-1, -1, -1):
#     print(zen[i])

    zen.reverse()

    for line in zen:
        print(line)