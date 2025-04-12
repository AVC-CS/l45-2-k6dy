import random


def main():
    total = 0
    numbers = []
    
    while total <= 100:
        num = random.randint(1, 10)
        numbers.append(num)
        total += num
        if total > 100:
            break
    
    total -= numbers[-1]

    print(f'The random values are {numbers}')
    print(f'The total is {total}')


    return numbers, total


if __name__ == '__main__':
    main()
