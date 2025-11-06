from collections import Counter





def using_dictionary(s: str) -> dict:
    count = {}
    for char in s:
        count[char] = count.get(char, 0)+1
    return count



print("************************* Usiong Dictionary  *************************")
text = "programming"
print(using_dictionary(text))

print("************************* Usiong Collections  *************************")

print(Counter(text))