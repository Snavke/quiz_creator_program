# dictionary to store inputs
dict_quiz = {}

question_number = 1

while True:
# Asks question
    question_input = input("Enter Question: ")
# Asks choices
    choice_labels = ['A', 'B', 'C', 'D']
    choices_dict = {}
    print ("Enter the 4 choices: ")
    for label in choice_labels:
        choice_text = input(f"Choice {label}: ")
        choices_dict[label] = choice_text
# Asks answer
    answer_input = input("Enter Answer (The Letter): ").upper

# Store data to dictionary
    dict_quiz[f"Question {question_number}"] = {
        "Question": question_input,
        "Choices": choices_dict,
        "Answer": answer_input
    }
    
    question_number += 1

# Confirm questions, choice, and answers, give option to redo & Add functionality to choose question to delete, or to edit (will overwrite)
    exit_prompt = input("Continue adding question? (yes/edit/delete/exit): ").lower()

    if exit_prompt == "edit":
        print ("\n Questions:")
        for items in dict_quiz:
            print (items)

        to_edit = input("Please enter the Question number to edit (number only): ")
        key = f"Question {to_edit}"
        if key in dict_quiz:
            print (f"\nEditing {key}")
            new_question = input ("Enter new question: ")

            print("Enter the new 4 choices: ")
            new_choices = {}
            for label in choice_labels:
                new_choice = input(f"Choice {label}: ")
                new_choices[label] = new_choice

            new_answer = input("Enter new correct answer (The letter): ").upper()
# Overwrites over the existing dictionary entry
            dict_quiz[key] = {
                "Question": new_question,
                "Choices": new_choices,
                "Answer": new_answer
            }
        else: 
            print ("Invalid question number.")
        


# Program terminates if yes
    if exit_prompt != "yes":
        print ("\nQuiz Summary: ")
        for question_id, data in dict_quiz.items():    
            print (f"\n{question_id}: {data['Question']}")
            for letter, choice in data['Choices'].items():
                print (f"    {letter}. {choice}")
            print (f"Answer: {data['Answer']}")
        break




# Store collected data per user "session" to text file