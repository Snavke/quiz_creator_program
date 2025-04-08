# dictionary to store inputs
dict_quiz = {}

question_number = 1

while True:
# Asks question
    question_input = input("Enter Question: ")
# Asks choices
    choice_labels = ['A', 'B', 'C', 'D']
    choices_dict = {}
    print ("Enter the 4 Choices: ")
    for label in choice_labels:
        choice_text = input(f"Choice {label}: ")
        choices_dict[label] = choice_text
# Asks answer
    answer_input = input("Enter Answer (The Letter): ")

# Store data to dictionary
    dict_quiz[f"Question {question_number}"] = {
        "Question": question_input,
        "Choices": choices_dict,
        "Answer": answer_input
    }
    
    question_number += 1

# Confirm questions, choice, and answers, give option to redo
    exit_prompt = input("Continue adding question? (yes/no): ").lower()
# Program terminates if yes
    if exit_prompt != "yes":
        print ("\nQuiz Summary: ")
        for question_id, data in dict_quiz.items():    
            print (f"\n{question_id}: {data['Question']}")
            for letter, choice in data['Choices'].items():
                print (f"    {letter}. {choice}")
            print (f"Answer: {data['Answer']}")
        break








# Add functionality to choose question to delete, or to edit (will overwrite)

# Store collected data per user "session" to text file