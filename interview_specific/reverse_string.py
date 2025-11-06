class Reverse_String:
    def reverse_str(self,strr):
        self.strr = strr
        print("Reverse String: ",''.join(reversed(self.strr)))

    def using_slicing(self,strr):
        print("Reversed String using slicing: ",self.strr[::-1])

    def using_loop(self,strr):
        reversed_txt=""
        for c in self.strr:
            reversed_txt = c + reversed_txt
        print(f"Reversed Text using loop:",reversed_txt)

r = Reverse_String()    
string_to_reverse = 'Hello World'    
r.reverse_str(string_to_reverse)
r.using_slicing(string_to_reverse)
r.using_loop(string_to_reverse)
