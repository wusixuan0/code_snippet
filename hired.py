def solution(arr):
    left = 0
    right = 0
    level = 0
    index = 1
    if len(arr) == 0:
      return ""
    
    for node in arr:
      print(index,level,2**(level+1))
      if level == 0:
        level = 1
        index += 1
        continue

      if node != -1:        
        if (index >= 2**level) and (index < 2**level+2**(level-1)):
          left += node
        elif (index >= 2**level+2**(level-1)) and (index < 2**(level+1)):
          right += node
      
      index += 1
      if (index == 2**(level+1)):
        print(index)
        level += 1
  		
    print(left, right)
    if left > right:
      
      return "Left"
    elif left < right:
      return "Right"
    else:
      return ""

test = [3, 6, 2, 9, -1, 10] #15 12
print(solution(test))