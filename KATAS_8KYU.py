'''
Lvl 7
Description:
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
'''
'''
BEST
def is_isogram(string):
    return len(string) == len(set(string.lower()))
'''
def is_isogram(string):
    l_string = string.lower()
    x = []
    for i in l_string:
        if i not in x:
            x.append(i)
        else:
            return False
    return True 


'''
Lvl 6
Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"
'''

'''
BEST 
def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
'''
def spin_words(sentence):
    x = sentence.split()
    for i in range(len(x)):
        if len(x[i]) >= 5:
            x[i] = x[i][::-1]
    return ' '.join(x)


'''
Lvl 6
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.
Note: If the number is a multiple of both 3 and 5, only count it once.
Courtesy of projecteuler.net (Problem 1)
'''
def solution(number):
    x = 0
    if number > 0:
        for i in range(number):
            if ((i % 3) == 0) or ((i % 5) == 0):
                x += i
        return x
    else:
        return 0
    
''' 
Lvl 7
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.

'''
def get_count(sentence):
    x = 0 
    for i in sentence:
        if i in ['a', 'e', 'i', 'o', 'u']:
            x += 1
    return x



'''
6KYU
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.
'''
def likes(names):
    if len(names) == 0:
        return("no one likes this")
    elif len(names) == 1:
        return(f"{names[0]} likes this")
    elif len(names) == 2:
        return(f"{names[0]} and {names[1]} like this")
    elif len(names) == 3:
        return(f"{names[0]}, {names[1]} and {names[2]} like this")
    else:
        return(f"{names[0]}, {names[1]} and {len(names)-2} others like this")

'''
6KYU
Implement a function that computes the difference between two lists. The function should remove all occurrences of elements from the first list (a) that are present in the second list (b). The order of elements in the first list should be preserved in the result.

Examples
If a = [1, 2] and b = [1], the result should be [2].

If a = [1, 2, 2, 2, 3] and b = [2], the result should be [1, 3].
'''
def array_diff(a, b):
    x = []
    for i in a :
        if i not in b:
            x.append(i)    
    return x

'''
Nathan loves cycling.
Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.
For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
'''
def litres(time):
    return int(time*0.5)
