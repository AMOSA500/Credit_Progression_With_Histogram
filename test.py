filepath = "progression.txt"
credit_list = []

def get_credits(filepath):
    """
    Returns a list of dictionaries with the 
    key being the course name and the value 
    being a list of credits
    """
    with open(filepath,"r") as file:
        numb_list = []
        for line in file:
            split_line = line.split(' - ') #splits the line into two parts
            numb_list = split_line[1].split(',') #splits the second part into a list
            numb_list = [int(i) for i in numb_list] #converts string to int
            credit_list.append({split_line[0]:numb_list}) # adds the key and value to the list
    return credit_list
