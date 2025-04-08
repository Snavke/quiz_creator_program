# dictionary to store inputs
dict_quiz = {}

# User provides questions
while True:
    question_input = input("Enter Question: ")
    choices_input = input("Enter 4 Possible Choices: ")
    answer_input = input("Enter Answer (The Letter): ")

    dict_question = {"Question": question_input,
                     "Choices": choices_input,
                     "Answer": answer_input
                     }
    

    exit_prompt = input("Continue adding question? (yes/no): ").lower()

    if exit_prompt != "yes":
        print ("Quiz Summary: ")
        break

print (dict_question)
# User provides possible choices

# User provides correct answer from possible choices



# Confirm questions, choice, and answers, give option to redo

# Continue asking until user chooses to terminate program

# Add functionality to choose question to delete, or to edit (will overwrite)

# Store collected data per user "session" to text file