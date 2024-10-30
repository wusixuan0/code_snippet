# To import queue datastructure
from collections import deque
queue = deque([2])
queue.append(3)
print(queue[1])
# Code to implement a binary tree
class TreeNode: 
     def __init__(self, val):
         self.val = val
         self.left = None
         self.right = None
  
class Solution(object):
  def levelOrder(self, root):
    queue = deque([root])
    result = []
    while queue:
      level = []
      
      for _ in range(len(queue)):
        
        node = queue.popleft()
        level.append(node.val)
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
        print("queue")
        for q in queue:
          print(q.val)
      result.append(level)
    return result
  
  def serialize(self, root):
        if root is None:
            return ""

        # use bfs to serialize the tree
        queue = deque([root])
        bfs_order = []
        while queue:
            node = queue.popleft()
            bfs_order.append(str(node.val) if node else '#')
            if node:
                queue.append(node.left)
                queue.append(node.right)

        return ' '.join(bfs_order)

  def deserialize(self, data):
        # None or ""
        if not data:
            return None

        bfs_order = [
            TreeNode(int(val)) if val != '#' else None
            for val in data.split()
        ]
        root = bfs_order[0]
        fast_index = 1

        nodes, slow_index = [root], 0
        while slow_index < len(nodes):
            print("slow node",slow_index, len(nodes),fast_index)
            node = nodes[slow_index]
            slow_index += 1
            node.left = bfs_order[fast_index]
            node.right = bfs_order[fast_index + 1]
            fast_index += 2

            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        return root      

  def binarySearch(self, nums, target):
    if len(nums) == 0 or nums == None:
      return -1
    start, end = 0, len(nums) - 1
    while start < end:
      mid = (start + end) //2
      if target == nums[mid]:
        end = mid
      elif target > nums[mid]:
        start = mid + 1
      else:
        end = mid - 1
    if nums[start] == target:
      return start
    return -1
  
  def maxDepth(self, root):
    if root is None:
        return 0
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
  def lowestCommonAncestor(self, root, A, B):
    # A & 下面有B => A
    # B & 下面有A => B
    # A & 下面啥都没有 => A
    # B & 下面啥都有 => B
    if root is None:
        return None

    if root == A or root == B:
        return root

    left_result = self.lowestCommonAncestor(root.left, A, B)
    right_result = self.lowestCommonAncestor(root.right, A, B)

    # A 和 B 一边一个
    if left_result and right_result:
        return root

    # 左子树有一个点或者左子树有LCA
    if left_result:
        return left_result

    # 右子树有一个点或者右子树有LCA
    if right_result:
        return right_result

    # 左右子树啥都没有
    return None
  def distanceK(self, root, target, K):
      def dfs(node, par = None):
          if node:
              node.par = par
              dfs(node.left, node)
              dfs(node.right, node)

      dfs(root)

      queue = deque([(target, 0)])
      seen = {target}
      while queue:
          if queue[0][1] == K:
              return [node.val for node, d in queue]
          node, d = queue.popleft()
          for nei in (node.left, node.right, node.par):
              if nei and nei not in seen:
                  seen.add(nei)
                  queue.append((nei, d+1))

      return []
  
  def fib(n, memo):
    if memo[n] != None:
      return memo[n]
    if n == 1 or n == 2:
      result = 1
    else:
      result = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = result
    return result

  def maxSubArray(self, nums):
        max_so_far = nums[0]
        max_global = nums[0]
        
        for i in range(1, len(nums)):
            max_so_far = max(nums[i], nums[i]+max_so_far)
            if (max_so_far>max_global):
                max_global = max_so_far
        return max_global
# root = [3,9,20,None,None,15,7] #[[3],[9,20],[15,7]]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
sol=Solution()
print(sol.maxDepth(root))


