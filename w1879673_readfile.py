
credit_list = []

def get_credits(filepath):
    """
    Returns a list of dictionaries with the 
    key being the course name and the value 
    being a list of credits
    """
    with open(filepath,"r") as file:
        for index, line in enumerate(file):
            if index == 0 or index == 1:
                pass
            else:
                line = [int(i) for i in line.split()]
                credit_list.append(line)
    
    return credit_list