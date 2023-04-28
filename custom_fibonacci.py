#fibonacci seriese using custom iterators
class fibbo_serries():
    def __init__(self, first_value, second_value, limit):
        self.first_value = first_value
        self.second_value = second_value
        self.limit = limit

    def __iter__(self):
        self.var = 1
        return self

    def __next__(self):
        if self.var <= self.limit:
            result = self.first_value
            self.first_value = self.second_value
            self.second_value = self.first_value + result
            self.var+=1
            return result
        raise StopIteration
    
FO = fibbo_serries(2,5,10)
for i in FO:
    print(i)