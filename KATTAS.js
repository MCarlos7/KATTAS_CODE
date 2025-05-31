/*6

Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
*/
function validBraces(str) {
  if (str === '') return true;
  const pairs = ['()', '[]', '{}'];

  for (let pair of pairs) {
    if (str.includes(pair)) {
      return validBraces(str.replace(pair, ''));
    }
  }

  return false;
}

/*5
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
Note: your solution must not modify the input array.


*/
function score(dice) {
  // Conteo de ocurrencias sin mutar el arreglo
  const counts = [0, 0, 0, 0, 0, 0, 0]; // índice 0 ignorado
  dice.forEach(n => counts[n]++);

  let total = 0;

  // Puntuación para tríos (1 tiene valor especial)
  const trioScores = [0, 1000, 200, 300, 400, 500, 600];
  for (let face = 1; face <= 6; face++) {
    if (counts[face] >= 3) {
      total += trioScores[face];
      counts[face] -= 3; // quita los dados usados en el trío
    }
  }

  // Puntuación para dados individuales (solo 1 y 5)
  total += counts[1] * 100;
  total += counts[5] * 50;

  return total;
}
/*6
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

*/
function sortArray(array) {
  let sorted = [];
  let odd = [];

  // Fase 1: Recorremos el arreglo original
  for (let i = 0; i < array.length; i++) {
    if (array[i] % 2 === 0) {
      // Si es par, lo colocamos en su lugar
      sorted.push(array[i]);
    } else {
      // Si es impar, marcamos con null y lo guardamos en 'odd'
      sorted.push(null);
      odd.push(array[i]);
    }
  }

  // Ordenamos los impares
  odd.sort((a, b) => a - b);

  // Fase 2: Rellenamos los nulls con los impares ordenados
  let oddIndex = 0;
  for (let i = 0; i < sorted.length; i++) {
    if (sorted[i] === null) {
      sorted[i] = odd[oddIndex];
      oddIndex++;
    }
  }

  return sorted;
}

/*

A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcissistic:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1652 (4 digits), which isn't:

    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
The Challenge:

Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10.

This may be True and False in your language, e.g. PHP.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.
*/
function narcissistic(value) {
  let str = value.toString();
  let length = str.length;
  let sum = 0;

  for (let i = 0; i < length; i++) {
    sum += Number(str[i]) ** length;
  }

  return sum === value;
}


/*6
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
Input = "The sunset sets at twelve o' clock."
Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
*/
function alphabetPosition(text) {
  let arr = [];
  for (let i = 0; i < text.length; i++) {
    let lower = text[i].toLowerCase();
    let code = lower.charCodeAt(0);
    if (code >= 97 && code <= 122) {
      let position = code - 96;
      arr.push(position);
    }
  }
  return arr.join(" ");
}

/* 7
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
*/

function digitalRoot(n) {
  if (n < 10) return n;

  let sum = 0;
  while (n > 0) {
    sum += n % 10;
    n = Math.floor(n / 10);
  }

  return digitalRoot(sum);
}


/* 7 
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
*/
function findShort(s) {
  let arr = s.split(' ');
  let short = arr[0].length;

  arr.forEach(palabra => {
    if (palabra.length < short) {
      short = palabra.length;
    }
  });

  return short;
}
/* 7
However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

Task
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
*/
var isSquare = function(n){
  return Math.sqrt(n) % 1 === 0; 
}
/*
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

*/
function duplicateCount(text) {
  const lower = text.toLowerCase();
  const charC = {};
  let count = 0;

  for (const x of lower) {
    charC[x] = (charC[x] || 0) + 1;
  }

  for (const y of Object.values(charC)) {
    if (y > 1) {
      count++;
    }
  }

  return count;
}


/* 7kiu
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.

Happy Coding!

*/
function squareDigits(num) {
  let total = '';
  let digits = Math.abs(num).toString();

  for (let i = 0; i < digits.length; i++) {
    let digit = Number(digits[i]);
    total += (digit * digit).toString();
  }

  return Number(total);
}

/* 6 kiu
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
*/
function solution(str){
  let arr = []
  for (let i = 0; i < str.length; i += 2){
    if (i + 1 >= str.length){
      arr.push(str[i] + '_');
    }else{
      arr.push(str[i] + str[i + 1]);
    }
  }
  return arr
}
