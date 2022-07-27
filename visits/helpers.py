'''A helper file for the visits app'''

def calculate_bmi(height, weight):
    height_in_metres = height/100
    bmi = weight/height_in_metres
    
    return bmi