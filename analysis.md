Task1-Sqrt

Time complexity of binary search takes O(logn) throwing a half in each iteration.
Space complexity is O(logn), the binary search recursive stack.

Task2 -Search in a rotated array

Time complexity is O(logn + 1 + logn) i.e. O(logn)
Space complexity is O(logn) the recursive stack of binary search

Task3 -Rearrange array

Time complexity is O(n log(n)) --> Just sort it and then apply the pattern iterating the array in reverse
Space complexity is O(n) as quicksort recursive stack have complexity O(n)

Task4- Dutch Flag

Time complexity is O(1) as iteration through the input list meaning O(n).
Space complexity is O(n) as the input_list n split in its 3 parts zeros, ones, twos, those combined sum O(n)

Task5- Autocomplete Tries

The worst case run time complexity O(l*n)
The length of words.(l)
The unique no. of chars at the same level.
The no. of words.(n)
The space complexity is of (O(word_length * unique_chars * no_of_words))

Task6- Unsorted array

Time complexity will be O(n).
AND Space complexity will be O(1).

TAsk7 -HTTP Router

Time Complexity:
insert will have O(n) complexity The insert operation saying that n = each '/', takes O(n) because there is one iteration per path part of it.
find : Almost the same process, iterating through input one time, O(n) complexity.
Space Complexity:
insert: path_parts occupies n but splitted, so takes O(n) complexity.
find: path_parts occupies n but splitted, so takes O(n) complexity.
