import re

class uncorrupt_computer:
    def __init__(self, path):
        self.machine_string = self.read_input(path)
        
    def read_input(self, path):
        
        reports = list()
        
        with open(path, 'r') as file:
            lines = file.readlines()
                
        return str(lines)
    
    def multiply(self, x, y):
        
        return x * y
    
    def correct_machine_code(self):
        
        calculation_values = [[int(calculation[1].strip(',').strip(')')), int(calculation[2].strip(',').strip(')'))] 
                              for calculation in re.findall(re.compile(r'(mul[(](\d*.)(\d*[)]))'), self.machine_string)]
    
        return sum([self.multiply(value[0], value[1]) for value in calculation_values])
    
    def correct_machine_code_dostate(self):
        
        calculation_values = list()
        do_state_values = re.split(re.compile(r"don[']t[(][)]"), self.machine_string)
        for idx, value in enumerate(do_state_values):
            if idx == 0:
                calculation_value = [[int(calculation[1].strip(',').strip(')')), int(calculation[2].strip(',').strip(')'))] 
                                      for calculation in re.findall(re.compile(r'(mul[(](\d*.)(\d*[)]))'), str(value))]
                calculation_values.extend(calculation_value)
            else:   
                do_search = re.findall(re.compile(r"do[(][)]"), str(value))

                if do_search:
                    value_filter = re.split(re.compile(r"do[(][)]"), value)
                    for idx, do_value in enumerate(value_filter):
                        if idx == 0:
                            print(len(do_value))
                        if idx != 0:    
                            calculation_value = [[int(calculation[1].strip(',').strip(')')), int(calculation[2].strip(',').strip(')'))] 
                                                  for calculation in re.findall(re.compile(r'(mul[(](\d*.)(\d*[)]))'), str(do_value))]
                            calculation_values.extend(calculation_value)
        
        return sum([self.multiply(value[0], value[1]) for value in calculation_values])
            

if __name__ == "__main__":
    
    path = r"C:\advent_code\day3\machine_string.txt"
    machine_code = uncorrupt_computer(path)
    print(f'This the total multiplication score: {machine_code.correct_machine_code()}')
    print(f'This is the total multiplication score for the dostate: {machine_code.correct_machine_code_dostate()}')