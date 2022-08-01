'''A helper file for the visits app'''

def calculate_bmi(height, weight):
    height_in_metres = int(height)/100
    weight = int(weight)
    bmi = weight/height_in_metres
    
    return int(bmi)