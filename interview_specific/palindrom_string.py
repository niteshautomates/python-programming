import re


def using_slicing(s: str)-> bool:
    return s == s[::-1]



def ignore_white_space(s: str) -> bool:
    s = s.replace(" ","").lower()
    return s == s[::-1]

def ignore_alphanumeric(s: str) -> bool:
    s = re.sub(r'[^a-zA-Z0-9]', '' ,s).lower()
    return s == s[::-1]

str1 = 'madam'    
str2 = 'hello'

print("************************* Usiong Slicing  *************************")
print(f"Is {str1} palindrome? ",using_slicing(str1))
print(f"Is {str2} palindrome? ",using_slicing(str2))
print("************************* Ignore case and white space  *************************")

print(f"Is {str1} palindrome? ",ignore_white_space(str1))
print(f"Is {str2} palindrome? ",ignore_white_space(str2))


print("************************* Ignorealpha numeric  *************************")
str1='A man, a plan, a canal: Panama'
print(f"Is {str1} palindrome? ",ignore_white_space('A man, a plan, a canal: Panama'))
print(f"Is {str2} palindrome? ",ignore_white_space('No lemon, no melon'))