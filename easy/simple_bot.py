"""
Simple Chatty Bot Project (JetBrains Academy)
For details, check out:
https://hyperskill.org/projects/97
"""

def greet(bot_name: str, birth_year: str) -> None:
    print(f'Hello! My name is {bot_name}.')
    print(f'I was created in {birth_year}.')


def remind_name() -> None:
    print('Please, remind me your name.')
    name: str = input()
    print(f'What a great name you have, {name}!')


def guess_age() -> None:
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    remainder_3: int = int(input())
    remainder_5: int = int(input())
    remainder_7: int = int(input())

    age: int = (remainder_3 * 70 + remainder_5 * 21 + remainder_7 * 15) % 105

    print(f"Your age is {age}; that's a good time to start programming!")


def count() -> None:
    print('Now I will prove to you that I can count to any number you want.')

    number_count: int = int(input())
    current: int = 0
    while current <= number_count:
        print(current, '!')
        current += 1


def test() -> None:
    print("Let's test your programming knowledge.")
    print('''Why do we use methods?
                1. To repeat a statement multiple times.
                2. To decompose a program into several small subroutines.
                3. To determine the execution time of a program.
                4. To interrupt the execution of a program.''')

    answer: int = int(input())

    if answer == 2:
        print('Completed, have a nice day!')
    else:
        print('Please, try again.')
        test()


def end() -> None:
    print('Congratulations, have a nice day!')


def main() -> None:
    greet('SimpleBot', '2022')
    remind_name()
    guess_age()
    count()
    test()
    end()


if __name__ == '__main__':
    main()
