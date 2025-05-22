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
