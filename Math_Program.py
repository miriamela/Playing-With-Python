import random


MILESTONE = 3


def main():
    correct_answers = 0
    while correct_answers != MILESTONE:
        number1 = random.randint(10, 99)
        number2 = random.randint(10, 99)
        result = number1+number2
        print("What is "+str(number1)+" + "+str(number2)+"?")
        answer = int(input("Your answer: "))
        if result == answer:
            correct_answers += 1
            print("Correct! You've gotten "+str(correct_answers)+" in a row")
            print(".")
        else:
            correct_answers = 0
            print("Incorrect. The expected answer is "+str(result))
    if correct_answers == MILESTONE:
        print("Congratulations! You have mastered addition")


if __name__ == "__main__":
    main()
