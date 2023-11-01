from graphics import *
from art import logo


print(logo)

# Data Table for the program
#  Variable declaration
start = True
position = 0
pass_data = []
fail_data = []
defer_data = []
student_record = []
outcome_label =['pass','defer','fail']
hightest_credit = 120
progression_dataset = [] # dictionary to store the progression outcome


# Credit Score Validation Function
def credit_validation(credit):
    if credit >= 0 and credit <= hightest_credit and credit % 20 == 0:
        return True
    else:
        return False    


# Progression Outcome Function     
def progression_outcome(credit_list):
    # unpack the list
    pass_credit = credit_list[0] 
    defer_credit = credit_list[1]
    fail_credit = credit_list[2]
    outcome_dict = {}
    
    # check the progression outcome
    if (pass_credit <= 40) and fail_credit >= 80:
        print('Exclude')
        outcome_dict['Exclude'] = f'{credit_list[0]},{credit_list[1]},{credit_list[2]}'
        progression_dataset.append(outcome_dict)
        
    elif pass_credit <= 80 and fail_credit <= 60:
        print('Module Retriever')
        outcome_dict['Module Retriever'] = f'{credit_list[0]},{credit_list[1]},{credit_list[2]}'
        progression_dataset.append(outcome_dict)
        
    elif (pass_credit == 100) and (defer_credit >= 0 or fail_credit >= 0):
        print('Module Trailer')
        outcome_dict['Module Trailer'] = f'{credit_list[0]},{credit_list[1]},{credit_list[2]}'
        progression_dataset.append(outcome_dict)
    else:
        print('Progress')
        outcome_dict['Progress'] = f'{credit_list[0]},{credit_list[1]},{credit_list[2]}'
        progression_dataset.append(outcome_dict)
    

# Histogram Function
def create_histogram(progression_dataset):
    number_of_progress = 0
    number_of_trailer = 0
    number_of_retriever = 0
    number_of_exclude = 0
    
    for item in progression_dataset:
        for key, value in item.items():
            if key == 'Progress':
                number_of_progress += 1
            elif key == 'Module Trailer':
                number_of_trailer += 1
            elif key == 'Module Retriever':
                number_of_retriever += 1
            else:  
                number_of_exclude += 1
        
        
    # Create a window
    # Graphical User Interface
    win = GraphWin('Histogram', 400, 400)
    win.setCoords(0, 0, 400, 400)
    win.setBackground('#dff9fb')
    
    text_center = Text(Point(200, 380), 'Histogram Results')
    text_center.draw(win)
    
    win.getMouse()
    win.close()



# Main Program
while start:
    '''This loop will run until the user quits the program'''
    try:
        if position >= 0 and position < len(outcome_label): # check if the position is within the range of the list
            credit = int(input(f'Please enter your credits at {outcome_label[position]}: '))
            if credit_validation(credit): # check if the input is within the range
                
                label = outcome_label[position]
                if label == 'pass':
                    pass_data.append(credit)
                elif label == 'defer':
                    defer_data.append(credit)
                else:
                    fail_data.append(credit)
                
                position += 1 # increment the position
                student_record.append(credit) # append the input to the list
                
            else:
                position = position # position remains the same
                print("Out of range or Score must be divisible by 20")
                
        else: # if the position is out of range
            print(f'Pass: {student_record[0]:4}\nDefer: {student_record[1]:3}\nFail: {student_record[2]:4}')
            total_credit = sum(student_record) # sum the list
            if total_credit != hightest_credit: # check if the total is equal to 120
                print('Total Incorrect. Start Again')
                student_record.clear() # clear the list
                position = 0
                continue
            else:
                # call the progression outcome function
                progression_outcome(credit_list=student_record) 
                
                # Clear, reset and restart
                restart = input('Q - Quit\nY - Yes\n').lower()
                if restart == 'y': # check if the user wants to quit
                    student_record.clear()
                    position = 0
                    continue 
                else:
                    create_histogram(progression_dataset)
                    # print the progression outcome after the user quits
                    for item in progression_dataset: # print the progression outcome
                        for key, value in item.items(): # unpack the dictionary
                            print(f'{key} - {value}') # print the outcome
                   
                    start = False
                
    except ValueError: # check if the input is an integer
        position = position
        print(f'Integer required')
        continue
        
    
    