/*
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

*/
#include <string>
#include <cctype>  // Para tolower

bool XO(const std::string& str) {
    int x = 0, o = 0;
    for (char c : str) {
        char lower = std::tolower(c);
        if (lower == 'x') {
            x++;
        } else if (lower == 'o') {
            o++;
        }
    }
    return x == o;
}

/* 6
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
*/

#include <vector>

int findOdd(const std::vector<int>& numbers){
  int x = 0;
  for (int i : numbers){
    x ^= i; 
  }
  return x;
}
