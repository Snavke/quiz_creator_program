# dictionary to store inputs
while True:  
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
        answer_input = input("Enter Answer (The Letter): ").upper()

    # Store data to dictionary
        dict_quiz[f"Question {question_number}"] = {
            "Question": question_input,
            "Choices": choices_dict,
            "Answer": answer_input
        }
        
        question_number += 1

# Confirm questions, choice, and answers, give option to redo & Add functionality to choose question to delete, or to edit (will overwrite)
      
        while True:   
            exit_prompt = input("Continue adding question? (yes/edit/delete/exit): ").lower()

        # To edit functionality
            if exit_prompt == "edit":
                print ("\n Questions:")
                for question_id in dict_quiz:
                    print (question_id)

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
        # To delete functionality
            elif exit_prompt == "delete":
                print ("\nQuestions:")
                for question_id in dict_quiz:
                    print (question_id)


                to_delete = input("Please enter the Question number to delete (number only): ")
                key = f"Question {to_delete}"
                if key in dict_quiz:
                    del dict_quiz[key]
                    print (f"Successfully deleted {key}.")
                else:
                    print ("Invalid question number.")
        # Continue outer loop (go back to add another question)
            elif exit_prompt == "yes":
                break


        # Program terminates and prints summary 
            elif exit_prompt == "exit":
                print ("\nQuiz Summary: ")
                for question_id, data in dict_quiz.items():    
                    print (f"\n{question_id}: {data['Question']}")
                    for letter, choice in data['Choices'].items():
                        print (f"    {letter}. {choice}")
                    print (f"Answer: {data['Answer']}")
                    
        # Store collected data per user "session" to text file   
                from datetime import datetime
                import os   
                
        # Creates a separate folder to store quiz txt files
                folder_name = "Quizzes"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)

                file_name = os.path.join(folder_name, datetime.now().strftime("%Y-%m-%d_%H-%M-%S.txt"))

                
                         
                with open(file_name, "w") as file:
                        file.write(f"Created New Quiz at - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                        file.write("\n" + "~"*40 + "\n")
                        
                        for question_id, data in dict_quiz.items():    
                            file.write (f"\n{question_id}: {data['Question']}\n")
                            for letter, choice in data['Choices'].items():
                                file.write (f"    {letter}. {choice}\n")
                        file.write (f"Answer: {data['Answer']}\n\n")
        
        # Inform user txt file is saved in within the program's folder
                import time
                print("Saving quiz", end='', flush=True)
                for msg in [" .", " ..", " ..."]:
                    time.sleep(0.5)
                    print(msg, end='', flush=True)
                print("\nDone! File saved as 'quiz_output.txt'")
                exit()

            else: 
                print ("Invalid input. Please enter yes/edit/delete/exit.")



