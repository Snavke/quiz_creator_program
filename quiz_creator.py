# dictionary to store inputs
dict_quiz = {}

question_number = 1

while True:
# Asks question
    question_input = input("Enter Question: ")
# Asks choices
    choices_input = input("Enter 4 Possible Choices: ")
# Asks answer
    answer_input = input("Enter Answer (The Letter): ")

# Store data to dictionary
    dict_quiz[f"Question {question_number}"] = {
        "Question": question_input,
        "Choices": choices_input,
        "Answer": answer_input
    }
    
    question_number += 1

# Confirm questions, choice, and answers, give option to redo
    exit_prompt = input("Continue adding question? (yes/no): ").lower()
# Program terminates if yes
    if exit_prompt != "yes":
        print ("\nQuiz Summary: ")
        for question_id, data in dict_quiz.items():    
            print (f"{question_id}: {data['Question']}")
            print (f"Choices: {data['Choices']}")
            print (f"Answer: {data['Answer']}")
        break








# Add functionality to choose question to delete, or to edit (will overwrite)

# Store collected data per user "session" to text file