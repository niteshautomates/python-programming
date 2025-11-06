class Sort_Numbers:
    
    def sort_number_with_string_as_input(self, str_input):
        numbers = str_input.split()
        sorted_number = numbers.sort(reverse=True)
        return ' '.join(numbers)
    
    def sort_number_sotring_with_list(self, str_input):
        numbers = list(map(int,str_input.split()))
        sorted_number = numbers.sort(reverse=True)
        return ' '.join(numbers)

user_input = input('Enter numbers to sort: ')
object = Sort_Numbers()
print(object.sort_number_with_string_as_input(user_input))    

print(object.sort_number_sorting_with_list(user_input))    