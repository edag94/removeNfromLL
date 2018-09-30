class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''to do in one pass iterate through the list, keeping a 
    n pointer when iterator becomes n+1, so you have a pointer tracking n-1 from end
    you need n-1 so that you can remove next and connect it to the removed nodes'''

class Solution:
    def __init__(self):
        self.head = None
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next and n == 1: 
            return None
        
        self.head = head
    
        node = self.iterate(head,n)
        
        return node
    
    
    def remove(self, node):
        leftL = node
        rightL = node.next.next
        leftL.next = rightL
    
    def iterate(self, head, n):
        loop_count = 0
        it = head
        prev_remove = None
        while(it):
            it = it.next
            if prev_remove:
                prev_remove = prev_remove.next
            loop_count = loop_count + 1
            if loop_count == n+1:
                prev_remove = head
        #last check in case of first node
        if loop_count == n:
                return head.next        
        else:
            self.remove(prev_remove)
            return self.head
        
if __name__ == '__main__':
    sol = Solution()
    one = ListNode(1)
    two = ListNode(2)
    one.next = two
    
    sol.removeNthFromEnd(one, 2)