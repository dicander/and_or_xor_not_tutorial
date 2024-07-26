import random


def ask_question():
    """ Query the user about an expression invovling and, or, xor, and maybe not
    Randomize the order of the operands and the operator
    There is a 10% chance that any operand will be negated
    There is a 33% chance of each operator being chosen
    Return 1 if the user answers correctly, 0 otherwise."""
    operator = random.choice(['and', 'or', 'xor'])
    left_operand = random.choice([True, False])
    right_operand = random.choice([True, False])
    left_not = random.choice([True, False, False, False, False, False, False, False, False, False])
    right_not = random.choice([True, False, False, False, False, False, False, False, False, False])
    question = ("(not " if left_not else "") + f'{left_operand}' + (")" if left_not else "") + f' {operator} ' \
               + ("(not " if right_not else "") + f'{right_operand}' + (")" if right_not else "")
    eval_question = question.replace("xor", "^")
    answer = eval(eval_question)
    user_answer = input(question + " = ")
    if user_answer.lower() == str(answer).lower():
        print("Correct!") 
        return 1
    else:
        print("Incorrect! The answer was " + str(answer))
        return 0
    

def main():
    # Ask the user 10 questions
    score = 0
    for _ in range(10):
        score += ask_question()
    print("You got", score, "out of 10 correct")


if __name__ == '__main__':
    main()