### Design decision
- The 4th problem I have implemented as a single traversal as per requirement with a space complexity of O(n) due to looping over a copy of the input array.  
- In the worst case in which all digits are zeros or twos the time complexity would be O(n²) due to the insert() and pop() methods which internally trigger a copying of all/several values to a new place which takes n times.
- Alternatively each number could be copied into a separate array and a concatenation of the three arrays in the desired order could be returned after looping over the input array. This approach would result in a time complexity of O(n) but since no specific time complexity was required I went with the inplace sorting approach.
