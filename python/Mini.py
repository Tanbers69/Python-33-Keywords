# Generator function using 'yield'
def even_numbers(limit):
    for num in range(limit):
        if num % 2 == 0:
            yield num  # using 'yield'

# Test the generator
for even in even_numbers(10):
    print("Even:", even)