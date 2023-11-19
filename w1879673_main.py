# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: W1879673
# Date: 19.11.2023

from graphics import *
from w1879673_art import logo
from w1879673_readfile import get_credits

# print the logo
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
    The function will append the dictionary to the list, outcome and number to the dictionary
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
    # Filepath to save the dictionary
    filepath = 'progression.txt'
    with open(filepath,'w') as file: # open the file
        file.write(data)
  

# Format Data Function
def format_data(data):
    '''
    This function will format the data
    The function will take a list as an argument
    The function will unpack the list and format the data
    The function will return a list
    # print(formatted_data) 
    # Pass    Defer   Fail\n
    # 120     0       0\n
    Reference: https://www.w3schools.com/python/ref_string_expandtabs.asp
    '''
    
    # Create a separator line
    headers = 'Pass\tDefer\tFail\tOutcome\n'
    separator = "-" * len(headers.expandtabs()) # expandtabs() method to expand the tab
    terminal_formatted_data = headers + separator + '\n'
    
    # Create a text file header
    text_file_header = 'Pass\tDefer\tFail\n'
    text_file_separator = "-" * len(text_file_header.expandtabs())
    text_format = text_file_header + text_file_separator + '\n'
    
    for item in data: # unpack the list {'Progress': '120,0,0'}
        for key, value in item.items(): # unpack the dictionary and get the value. Ex: 120,0,0
            value = value.split(',') # split the value into a list
            # <: left align
            terminal_formatted_data += f'{value[0]:<4}\t{value[1]:<5}\t{value[2]:<4}\t{key:<7}\n' 
            text_format += f'{value[0]:<4}\t{value[1]:<5}\t{value[2]:<4}\n' 
    # call the store file function
    store_file(text_format)   
        
    return terminal_formatted_data


# Histogram Function
def create_histogram(progression_dataset):
    '''
    This function will create a histogram
    The function will take a list as an argument
    The function will unpack the list and count the number of each progression outcome
    The function will create a window and draw a histogram
    The function will draw a bar for each progression outcome and display the number of each progression outcome
    The progress bar is filled with a different colour and 20 pixels was added to the height
    Reference: https://www.geeksforgeeks.org/python-pil-imagedraw-draw-rectangle/
    
    '''
        
    # Create a window
    # Graphical User Interface
    win = GraphWin('Histogram', 400, 400)
    win.setCoords(0, 0, 400, 400)
    win.setBackground('#dff9fb')
    
    text_center = Text(Point(200, 380), 'Histogram Results')
    text_center.draw(win)
    
    # Create a bar for Progress
    colour_list = ['#78e08f', '#b8e994', '#079992', '#e55039'] # list of colours
    i = 0
    bar_width = 70 # width of the bar
    bar_spacing = 10 # spacing between the bars
    x = bar_spacing # x coordinate
    label_space = 50 # y coordinate
    total = 0 # total number of each progression outcome
    

    for key, value in outcome_label.items(): # unpack the dictionary
        total += value # sum the value
        progress_bar = Rectangle(Point(x, label_space), Point(x + bar_width, label_space + (value*20))) # create a bar
        progress_bar.setFill(colour_list[i]) # fill the bar with a colour
        progress_bar.draw(win)  # draw the bar
        
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
        

# Main Program Starts Here
filepath = "progression.txt" # filepath to read the file
read_file = input('Do you have Data in progression.txt file to read?\nY - Yes\nN - No - Enter Manually\n').lower()
while start:
    '''
    This loop will run until the user quits the program
    Position is used to keep track of the list index
    The loop will take the user input and append it to the list
    The loop will check if the input is within the range,an integer, and divisible by 20
    progression.txt file will be read if the user enters 'y'
    NB: Follow the pattern to enter the credits
    '''
    try:
        
        if read_file == 'n':
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
                        
                        # call the histogram function
                        create_histogram(progression_dataset)
                        
                        # clear the list
                        student_record.clear()
                        break 
                    
        # read the file if the user enters 'y'
        else:
            input('Press Enter to read the file\n')
            credit_list = get_credits(filepath)
            credit_sum = 0
            len_list = len(credit_list) # get the length of the list
            x = 0 
            if credit_list:
                for items in credit_list:
                    for item in items:
                        if credit_validation(item): # check if the input is within the range
                            credit_sum += item # sum the list
                        else:
                            print("Out of range. Please check the file, credit must be within 0 and 120 and divisible by 20")
                            credit_sum = 0
                            break
                    if credit_sum == hightest_credit:
                        # Pass list to progression_outcome function
                        progression_outcome(credit_list=items) 
                        credit_sum = 0
                        x += 1
                    else:
                        print('Total Incorrect for one of your records. Please check the file, total must be 120')
                        credit_sum = 0
                        break
                    
                # print the progression outcome after the user quits
                if x == len_list:
                    formatted_data =  format_data(progression_dataset)
                    print(formatted_data)
                                    
                    # call the histogram function
                    create_histogram(progression_dataset)
                    break 
            else:
                print('No Data in the file')
                break
    except ValueError: # check if the input is an integer
        position = position
        print(f'Integer required')
        if read_file == 'y':
            print('Please check the file, credit must be an integer')
            progression_dataset.clear()
        continue
        
    
    