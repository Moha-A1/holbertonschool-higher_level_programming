#!/usr/bin/python3

# Copier la fonction
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    my_list[idx] = element
    return my_list

# Tests
print("=== Test 1: Index valide ===")
my_list = [1, 2, 3, 4, 5]
print(f"Liste originale: {my_list}")
result = replace_in_list(my_list, 3, 9)
print(f"Après remplacement: {result}")
print(f"Liste modifiée: {my_list}")
print()

print("=== Test 2: Index négatif ===")
my_list2 = [1, 2, 3, 4, 5]
result2 = replace_in_list(my_list2, -1, 99)
print(f"Index -1: {result2}")
print()

print("=== Test 3: Index trop grand ===")
my_list3 = [1, 2, 3, 4, 5]
result3 = replace_in_list(my_list3, 10, 99)
print(f"Index 10: {result3}")
