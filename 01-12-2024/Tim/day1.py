class list_distances:
    def __init__(self, path):
        self.list1, self.list2 = self.read_input(path)
        
    def read_input(self, path):
        
        list1 = list()
        list2 = list()
        
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                list1.append(int(line.split()[0]))
                list2.append(int(line.split()[1]))
                
        return sorted(list1), sorted(list2)
    
    def calculate_total_distance(self):
        
        return sum([abs(value - self.list2[idx]) for idx, value in enumerate(self.list1)])
    
    def calculate_similarity(self):
        
        similarity_score = 0
        for value in self.list1:
            similarity_score += value * len([value2 for value2 in self.list2 if value==value2])
            
        return similarity_score
                       
if __name__ == "__main__":
    locations = list_distances(r"C:\advent_code\lists.txt")
    print(f'This is the total distance: {locations.calculate_total_distance()}')
    print(f'This is the similarity score: {locations.calculate_similarity()}')
            
        