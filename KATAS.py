'''3kiu
Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.

For Sudoku rules, see the Wikipedia article.

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)
# Should return
 [[5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]]
'''
def sudoku(puzzle):
    solve = True
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                opciones = [1,2,3,4,5,6,7,8,9]

                
                for num in puzzle[i]:
                    if num in opciones:
                        opciones.remove(num)

                
                for fila in puzzle:
                    if fila[j] in opciones:
                        opciones.remove(fila[j])

                
                start_row = (i // 3) * 3
                start_col = (j // 3) * 3
                for r in range(3):
                    for c in range(3):
                        valor = puzzle[start_row + r][start_col + c]
                        if valor in opciones:
                            opciones.remove(valor)

                if len(opciones) == 1:
                    puzzle[i][j] = opciones[0]
                else:
                    puzzle[i][j] = 0
                    solve = False

    if solve:
        return puzzle
    else:
        return sudoku(puzzle)
# It's OK. I think I have a good approach, the best practices look weird xd

'''
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.


'''
def format_duration(seconds):
    if seconds == 0:
        return "now"

    result = ""
    units = {"year": 31536000, "day": 86400, "hour": 3600, "minute": 60, "second": 1}
    parts = []

    for unit in units:
        value = seconds // units[unit]
        seconds -= value * units[unit]

        if value >= 1:
            part = f"{value} {unit}"
            if value != 1:
                part += "s"
            parts.append(part)

    if len(parts) == 1:
        result = parts[0]
    else:
        result = ", ".join(parts[:-1]) + " and " + parts[-1]

    return result

'''
The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80 

Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the same manner as in the drawing:

alternative text

Hint:
See Fibonacci sequence

Ref:
http://oeis.org/A000045

The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and returns the total perimeter of all the squares.

perimeter(5)  should return 80
perimeter(7)  should return 216
'''
def perimeter(n):
    a, b = 0, 1
    for _ in range(n + 3):
        a, b = b, a + b
    return 4 * (a - 1 )

'''4KYU
Write a function called sumIntervals/sum_intervals that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

Intervals
Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

Overlapping Intervals
List containing overlapping intervals:

[
   [1, 4],
   [7, 10],
   [3, 5]
]
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.

Examples:
sumIntervals( [
   [1, 2],
   [6, 10],
   [11, 15]
] ) => 9

sumIntervals( [
   [1, 4],
   [7, 10],
   [3, 5]
] ) => 7

sumIntervals( [
   [1, 5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ) => 19

sumIntervals( [
   [0, 20],
   [-100000000, 10],
   [30, 40]
] ) => 100000030
Tests with large intervals
Your algorithm should be able to handle large intervals. All tested intervals are subsets of the range [-1000000000, 1000000000].
'''
def sum_of_intervals(intervals):
    total = 0
    merged = []

    for current in intervals:
        a, b = sorted(current)  # Ordena el intervalo por si viene invertido
        new_interval = [a, b]
        updated = []

        for m in merged:
            # Si se superponen, fusionarlos
            if not (new_interval[1] <= m[0] or new_interval[0] >= m[1]):
                new_interval[0] = min(new_interval[0], m[0])
                new_interval[1] = max(new_interval[1], m[1])
            else:
                updated.append(m)

        # Agrega el nuevo intervalo fusionado a la lista
        updated.append(new_interval)
        merged = updated

    # Sumar longitudes
    for i in merged:
        total += i[1] - i[0]

    return total

'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
'''
def rgb(r, g, b):
    return to_hex(r) + to_hex(g) + to_hex(b)



def to_hex (x):
    hexV = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    
    if x < 0:  #Check values in range 
        x = 0
    elif x > 255:
        x = 255
        
    high = x // 16
    low = x % 16
    return hexV[high] + hexV[low]
#BEST
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))



'''
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False


'''
def scramble(s1, s2):
    x = {}

    for c in s1:
        x[c] = x.get(c, 0) + 1

    for c in s2:
        if x.get(c, 0) == 0:
            return False
        x[c] -= 1

    return True

'''
5kyu ????? 
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
'''
def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02}:{minutes:02}:{secs:02}"
'''
5kyu
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''
def pig_it(text):
    split = text.split()
    final = ''
    for i in split:
        if i.isalpha(): 
            new_word = i[1:] + i[0] + 'ay'
        else:
            new_word = i
        final += new_word + ' '
    return final.strip()

''' i LOVE THIS CODE 
5kyu
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
'''
def zero(fn=0):  return 0 if (fn == 0) else  fn(0)
def one(fn=0):   return 1 if (fn == 0) else  fn(1)
def two(fn=0):   return 2 if (fn == 0) else  fn(2)
def three(fn=0): return 3 if (fn == 0) else  fn(3)
def four(fn=0):  return 4 if (fn == 0) else  fn(4)
def five(fn=0):  return 5 if (fn == 0) else  fn(5)
def six(fn=0):   return 6 if (fn == 0) else  fn(6)
def seven(fn=0): return 7 if (fn == 0) else  fn(7)
def eight(fn=0): return 8 if (fn == 0) else  fn(8)
def nine(fn=0):  return 9 if (fn == 0) else  fn(9)

def plus(fn):        return lambda x: x + fn
def minus(fn):       return lambda x: x - fn
def times(fn):       return lambda x: x * fn
def divided_by(fn):  return lambda x: x // fn



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
