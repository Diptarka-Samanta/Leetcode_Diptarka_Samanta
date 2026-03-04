from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        res = []
        q = deque([root]) if root else deque()
        while q:
            level = []
            length = len(q)
            for i in range(length):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if len(res) % 2 == 1:
                level.reverse()
            res.append(level)
        return res