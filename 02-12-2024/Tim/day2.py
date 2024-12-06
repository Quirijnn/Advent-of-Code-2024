class report_evaluation:
    def __init__(self, path):
        self.reports = self.read_input(path)
        
    def read_input(self, path):
        
        reports = list()
        
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                reports.append([int(value) for value in line.split()])
                
        return reports
    
    def safety_analysis(self, report):
        
        direction_tracker = 0
        for idx, report_value in enumerate(report):
            if idx + 1 == len(report):
                continue
            elif 1 <= abs(report[idx + 1] - report_value) <= 3:
                if direction_tracker == 0:
                    direction_tracker = report_value - report[idx + 1]
                elif direction_tracker < 0 and report_value - report[idx + 1] > 0:
                        return False
                elif direction_tracker > 0 and report_value - report[idx + 1] < 0:
                        return False     
            else:
                return False
        
        return True
    
    def safety_dampner(self, report):
        
            return any([self.safety_analysis([report_value for idx, report_value in enumerate(report) if i != idx ])
                         for i in range(len(report))])
                
    def calculate_safety(self):
        
        return len([report for report in self.reports if self.safety_analysis(report)])
    
    def calculate_safety_with_dampner(self):
        
        reports_dampned = list()
        for report in self.reports:
            if not self.safety_analysis(report):
              if self.safety_dampner(report):
                  reports_dampned.append(report)    
            else:
                reports_dampned.append(report)
                
        return len(reports_dampned)
            
if __name__ == "__main__":
    
    path = r"C:\advent_code\day2\reports.txt"
    evaluation = report_evaluation(path)
    print(f'These are the total amount of safe reports: {evaluation.calculate_safety()}')
    print(f'These are the total amount of dampned safe reports: {evaluation.calculate_safety_with_dampner()}')