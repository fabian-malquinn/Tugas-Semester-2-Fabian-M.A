def contains_even_numbers(x):
    for i in x:
        if i % 2 == 0:
            print("list berisi bilangan genap")
            break
        else:
            print("list tidak berisi bilangan genap")


print("For List 1: ")
contains_even_numbers([1, 3, 5])
print("\nFor List 2: ")
contains_even_numbers([2, 4, 6])
