'''
5kyu
The Fibonacci numbers are the numbers in the following integer sequence (Fn): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such that:

F(0)=0
F(1)=1
F(n)=F(n−1)+F(n−2)
Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying:

F(n)∗F(n+1)=prod
Your function takes an integer (prod) and returns an array/tuple (check the function signature/sample tests for the return type in your language):

if F(n) * F(n+1) = prod:
(F(n), F(n+1), true)
If you do not find two consecutive F(n) verifying F(n) * F(n+1) = prod:
(F(n), F(n+1), false)
where F(n) is the smallest one such as F(n) * F(n+1) > prod.
Examples:
714 ---> (21, 34, true)
--> since F(8) = 21, F(9) = 34 and 714 = 21 * 34

800 --->  (34, 55, false)
--> since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55

'''

def product_fib(_prod):
    a, b = 0, 1
    while a * b < _prod:
        a,b = b, a+b
    return [a, b, a*b == _prod]



'''
5kyu
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
'''
def cakes(recipe, available):
    first = True
    for i in recipe:
        
        if i in available:
            
            available_cakes = available[i]//recipe[i]
            
            if first:  #can't use inf
                cakes = available_cakes
                first = False
                
                
            elif available_cakes < cakes:
                cakes = available_cakes
                
        else:
            return 0
            
    return cakes

'''
6 KYU
Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.
Modern Roman numerals are written by expressing each digit separately starting with the leftmost digit and skipping any digit with a value of zero. There cannot be more than 3 identical symbols in a row.
In Roman numerals:

1990 is rendered: 1000=M + 900=CM + 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII.
1666 uses each Roman symbol in descending order: MDCLXVI.
Example:

   1 -->       "I"
1000 -->       "M"
1666 --> "MDCLXVI"
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
More about roman numerals
'''

def solution(n):
    # TODO convert int to roman string
    SOLUCION = ""
    UNIDADES = {"1":"I","2":"II","3":"III","4":"IV","5":"V","6":"VI","7":"VII","8":"VIII","9":"IX" }
    DECENAS  = {"1":"X","2":"XX","3":"XXX","4":"XL","5":"L","6":"LX","7":"LXX","8":"LXXX","9":"XC" }
    CENTENAS = {"1":"C","2":"CC","3":"CCC","4":"CD","5":"D","6":"DC","7":"DCC","8":"DCCC","9":"CM" }
    MILLARES = {"1":"M","2":"MM","3":"MMM"}
    
    numero_str = str(n).zfill(4)
    if numero_str[0] != "0":
        SOLUCION += MILLARES.get(numero_str[0], "")
    if numero_str[1] != "0":
        SOLUCION += CENTENAS.get(numero_str[1], "")
    if numero_str[2] != "0":
        SOLUCION += DECENAS.get(numero_str[2], "")
    if numero_str[3] != "0":
        SOLUCION += UNIDADES.get(numero_str[3], "")
        
    return SOLUCION

'''
7 KYU
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
6 KYU
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
6 KYU
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
7 KYU
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
