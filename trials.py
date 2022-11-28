"""Python functions for JavaScript Trials 1."""
items = [1, 'hello', True]

def output_all_items(items):
    # TODO: replace this line with your code
    for item in items:
        print(item)

# output_all_items(items)


def get_all_evens(nums):
    # TODO: replace this line with your code
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums

# print(get_all_evens())

def get_odd_indices(items):
    # TODO: replace this line with your code
    odd_indices = []
    for i in range(len(items)):
        if i % 2 == 1:
            odd_indices.append(items[i])

    return odd_indices

# print(get_odd_indices([1, 'hello', True, 500]))

def print_as_numbered_list(items):
    # TODO: replace this line with your code
    for i in range(len(items)):
        print(f"{i+1}. {items[i]}")

# print_as_numbered_list([1, 'hello', True, 500])


def get_range(start, stop):
    # TODO: replace this line with your code
    nums = []
    for i in range(start, stop):
        nums.append(i)

    return nums

# print(get_range(1, 5))

def censor_vowels(word):
    # TODO: replace this line with your code

    censor_vowels_list = []
    for letter in word:
        if letter in 'aeiou':
            censor_vowels_list.append('*')
        else:
            censor_vowels_list.append(letter)
    
    return "".join(censor_vowels_list)

# print(censor_vowels('hello'))


def snake_to_camel(string):
    # TODO: replace this line with your code
    camelCase = []
    for word in string.split('_'):
        camelCase.append(word[0].upper() + word[1:])

    return "".join(camelCase)

# print(snake_to_camel('hello_world'))

def longest_word_length(words):
    # TODO: replace this line with your code
    longest = len(words[0])
    
    for word in words:
        if len(word) > longest:
            longest = len(word)
    
    return longest

# print(longest_word_length(['zebra', 'jellyfish']))


def truncate(string):
    # TODO: replace this line with your code
    result = []

    for letter in string:
        if len(result) == 0 or letter != result[-1]:
            result.append(letter)

    return "".join(result)

# print(truncate('aaaabbbbcccca'))

def has_balanced_parens(string):
    # TODO: replace this line with your code
    parens = 0
    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
    
    if parens < 0:
        return False

    return parens == 0

# print(has_balanced_parens('(Oh no!)()'))



def compress(string):
    # TODO: replace this line with your code
    #   > compress('Hello, world! Cows go moooo...');
    #   'Hel2o, world! Cows go mo4.3'
    compressed = []

    curr_char = ""
    count_char = 0
    for char in string:
        if char != curr_char:
            compressed.append(curr_char)

            if count_char > 1:
                compressed.append(str(count_char))

            curr_char = char            # Hel
            count_char = 0

        count_char += 1                 # 1 2

    compressed.append(curr_char)
    if count_char > 1:
        compressed.append(str(count_char))
    
    return "".join(compressed)

# print(compress('Hello, world! Cows go moooo...'))
