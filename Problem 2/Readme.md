O(n^2) solution

(def bounds_of_rotations) solution:


idea: calculate weighted sum of list for each component, rotate and recompute saving it. Then use min and max to find solution


O(2n) solution round off to O(n) (bonus part 1)


idea: since the weighted value c is a linear increase in power, its possible to reduce the complexity by dividing the entire sum by c and adding back the value with the highest value of c that is removed thus effectively 'rotating the list and bringing the first variable to the back' and getting the rotated value to see if its larger or smaller.


O(2n) solution round off to O(n) (bonus part 2)

idea: by subtracting the sum of list and adding the len(lis) * variable that is remove completely, is the same as bonus 1 where instead of dividing it is subtracting to remove smallest variable and bringing it to the back
