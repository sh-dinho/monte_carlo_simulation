# Write a class that calculates and stores the height and weight of a person in metric. The file should be named lab.py.  
# BMI is calculated using this formula:
# Weight/Height^2 - weight is in kilograms and height is in meters.
# The class should have two properties named:

#     Weight
#     Height

# The class should have two methods:

#     BMI_Value – This takes no arguments and returns a decimal value of the BMI
#     Equals – This should override the equals method from the object class to
# compare the weight and height of two BMI objects.  
# To override the equal method you should implement this method: __eq__(self, other) and return a boolean

class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        
    def BMI_Value(self):
        return self.weight / (self.height ** 2)
    
    def __eq__(self, other):
        return self.weight == other.weight and self.height == other.height
    
    def __str__(self):
        return f'Weight: {self.weight}, Height: {self.height}'
    
    def __compare__(self, other):
        if self.weight == other.weight and self.height == other.height:
            return True
        else:
            return False 
        
    def __init__(self, Weight, Height):
        BMI.__init__(self,Weight,Height)
        self.Weight = Weight
        self.Height = Height
        
        