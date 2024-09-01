with open('numbers.txt', 'r', encoding='utf-8') as file:
    nums = file.readlines()
    num_list = []

    for line in nums:
        for elem in line.split():
            try:
                elem = int(elem)
                num_list.append(elem)
            except:
                continue
    answer = sum(num_list)
    print(answer)

with open('answer.txt', 'w', encoding='utf-8') as file:
    file.write(str(answer))