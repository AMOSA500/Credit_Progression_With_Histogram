from graphics import *
from art import logo


print(logo)


#  Variable declaration
start = True # boolean value to start the program
position = 0 # position to keep track of the list index
student_record = [] 
input_label =['pass','defer','fail'] # list to store the outcome label
outcome_label = {} # dictionary to store the outcome label and total number of each outcome
hightest_credit = 120 # highest credit
progression_dataset = [] # dictionary to store the progression outcome


# Credit Score Validation Function
def credit_validation(credit):
    '''
    This function will check if the credit is within the range
    The function will take an integer as an argument
    The function will return a boolean value
    '''
    return credit >= 0 and credit <= hightest_credit and credit % 20 == 0
     

# Progression Outcome Function     
def progression_outcome(credit_list):
    '''
    This function will check the progression outcome
    The function will take a list as an argument
    The function will append a dictionary of outcome_dict into the progression_dataset list
    The function will unpack the list and check the progression outcome
    The function will append the dictionary to the list
    The function will append the outcome and number to the dictionary
    Reference: https://www.w3schools.com/python/python_dictionaries.asp
    
    Ex: {'Progress': '120,0,0'}
    '''
    # unpack the list
    pass_credit = credit_list[0] 
    defer_credit = credit_list[1]
    fail_credit = credit_list[2]
    outcome_dict = {} # dictionary to store the progression outcome
    
    # check the progression outcome
    display_value = f'{credit_list[0]},{credit_list[1]},{credit_list[2]}'
    
    if (pass_credit <= 40) and fail_credit >= 80:
        print('Exclude')
        outcome_dict['Exclude'] = display_value # Create a dictionary
        # Count or update the number of each progression outcome
        if 'Exclude' in outcome_label: # check if the key is in the dictionary
            outcome_label['Exclude'] += 1 # increment the value 
        else:
            outcome_label['Exclude'] = 1
        
            
    elif pass_credit <= 80 and fail_credit <= 60:
        print('Module Retriever')
        outcome_dict['Module Retriever'] = display_value
        # Count or update the number of each progression outcome
        if 'Retriever' in outcome_label:
            outcome_label['Retriever'] += 1
        else:
            outcome_label['Retriever'] = 1
        
    elif (pass_credit == 100) and (defer_credit >= 0 or fail_credit >= 0):
        print('Progress (Module Trailer)')
        outcome_dict['Module Trailer'] = display_value
        # Count or update the number of each progression outcome
        if 'Trailer' in outcome_label:
            outcome_label['Trailer'] += 1
        else:
            outcome_label['Trailer'] = 1
    
    else:
        print('Progress')
        outcome_dict['Progress'] = display_value
        # Count or update the number of each progression outcome
        if 'Progress' in outcome_label:
            outcome_label['Progress'] += 1
        else:
            outcome_label['Progress'] = 1
        
    
    # append the dictionary to the list        
    progression_dataset.append(outcome_dict) # append all outcome_dict dictionary to the list


# Store file in a text file
def store_file(data):
    '''
    This function will store the progression outcome in a text file
    The function will take a list as an argument
    The function will unpack the list and write the outcome to the file
    Reference: https://www.w3schools.com/python/python_file_write.asp
    '''
    # s_no = 0 # serial number
    with open('progression.txt','w') as file: # open the file
        for item in data: # unpack the list
            for key, value in item.items(): # unpack the dictionary
                s_no += 1 # increment the serial number
                file.write(f'str{s_no}. str{key} - str{value}\n') # write to the file
  

def format_data(data):
    '''
    This function will format the data
    The function will take a list as an argument
    The function will unpack the list and format the data
    The function will return a list
    '''
    formatted_data = ''
    for item in data: # unpack the list
        for key, value in item.items(): # unpack the dictionary
            formatted_data += f'{key} - {value}\n' # format the data
    return formatted_data # return the formatted data


# variables to store the number of each progression outcome
number_of_progress = number_of_trailer = number_of_retriever = number_of_exclude = 0 

# Calculate progress outcome
def calculate_progress_outcome(data): 
    '''
    This function will calculate the amount of progression outcome
    The function will take a list as an argument
    The function will unpack the list and calculate each progression outcome
    The function will set the value to a variable
    The function will return the variable
    The function has a global variable to store the number of each progression outcome
    Reference: https://www.w3schools.com/python/python_dictionaries_loop.asp
    '''
    global number_of_progress, number_of_trailer, number_of_retriever, number_of_exclude
    
    for item in progression_dataset:
        # unpack the dictionary
        # _ is used to ignore the value
        for key, _ in item.items(): 
            if key == 'Progress':
                number_of_progress += 1
            elif key == 'Module Trailer':
                number_of_trailer += 1
            elif key == 'Module Retriever':
                number_of_retriever += 1
            else:  
                number_of_exclude += 1
    

# Histogram Function
def create_histogram(progression_dataset):
    '''
    This function will create a histogram
    The function will take a list as an argument
    The function will unpack the list and count the number of each progression outcome
    The function will create a window and draw a histogram
    Reference: https://www.geeksforgeeks.org/python-pil-imagedraw-draw-rectangle/
    
    '''
    calculate_progress_outcome(progression_dataset)
        
    # Create a window
    # Graphical User Interface
    win = GraphWin('Histogram', 400, 400)
    win.setCoords(0, 0, 400, 400)
    win.setBackground('#dff9fb')
    
    text_center = Text(Point(200, 380), 'Histogram Results')
    text_center.draw(win)
    
    # Create a bar for Progress
    colour_list = ['#78e08f', '#b8e994', '#079992', '#e55039']
    len_dataset = len(outcome_label)
    i = 0
    bar_width = 100
    bar_spacing = 10
    x = bar_spacing
    label_space = 50
    total = 0
    

    for key, value in outcome_label.items():
        total += value
        progress_bar = Rectangle(Point(x, label_space), Point(x + bar_width, label_space + (value*20))) 
        progress_bar.setFill(colour_list[i])
        progress_bar.draw(win)
        
        # Create a text for Progress
        top_text = Text(Point(x + (bar_width/2), label_space + (value*30)), value)
        top_text.draw(win)
        
        # Create a bottom text for Progress
        bottom_text = Text(Point(x + (bar_width /2), label_space - 10),  key)
        bottom_text.setSize(8)
        bottom_text.draw(win)
        i += 1
        x += bar_width + bar_spacing
    
    bottom_text = Text(Point(50, label_space - 30),  f'Total: {total}')
    bottom_text.setSize(8)
    bottom_text.draw(win)
    
    try:
        student_record.clear() # clear the list
        progression_dataset.clear() # clear the list
        win.getMouse() # keep the window open
        win.close() # close the window
    except GraphicsError:
        print("Window Closed")
        

# Main Program
while start:
    '''
    This loop will run until the user quits the program
    Position is used to keep track of the list index
    The loop will take the user input and append it to the list
    The loop will check if the input is within the range
    The loop will check if the input is an integer
    The loop will check if the input is divisible by 20
    '''
    try:
        if position >= 0 and position < len(input_label): # check if the position is within the range of the list
            credit = int(input(f'Please enter your credits at {input_label[position]}: '))
            if credit_validation(credit): # check if the input is within the range
                position += 1 # increment the position
                student_record.append(credit) # append the input to the list
                
            else:
                position = position # position remains the same
                print("Out of range")
                
        else: # if the position is out of range
            print(f'Pass: {student_record[0]:4}\nDefer: {student_record[1]:3}\nFail: {student_record[2]:4}')
            total_credit = sum(student_record) # sum the list
            if total_credit != hightest_credit: # check if the total is equal to 120
                print('Total Incorrect')
                student_record.clear() # clear the list
                position = 0
                continue
            else:
                # call the progression outcome function
                progression_outcome(credit_list=student_record) 
                print("*** ------RESTART------- ***")
                # Clear, reset and restart
                restart = input('Q - Quit\nY - Continue\n').lower()
                if restart == 'y': # check if the user wants to quit
                    student_record.clear()
                    position = 0
                    continue 
                else:
                    # print the progression outcome after the user quits
                    # Ex: {'Progress': '120,0,0'}
                    formatted_data =  format_data(progression_dataset)
                    print(formatted_data)
                    
                    # print the number of each progression outcome
                    print(outcome_label)
                    
                    # call the histogram function
                    create_histogram(progression_dataset)
                    
                    # call the store file function
                    store_file(progression_dataset)
                    
                    # clear the list
                    student_record.clear()
                    # stop the loop
                    # start = False
                    break  
                                
                    
                
    except ValueError: # check if the input is an integer
        position = position
        print(f'Integer required')
        continue
        
    
    