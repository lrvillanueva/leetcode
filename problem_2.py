# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       l1_current = l1
        l2_current = l2
        carry = 0
        output = ListNode()
        temp = output

        # currently still numbers in both L1 and L2
        while l1_current != None and l2_current != None:

            # Calculate sum and carry and save into current Node
            total = l1_current.val+l2_current.val+carry
            carry = total // 10
            temp.val = total % 10

            # Iterate to next Node in L1 and L2
            l1_current = l1_current.next
            l2_current = l2_current.next

            # Reached the end of both lists
            if l1_current == None and l2_current == None:
                    if carry == 1: # Still a Carry, create 1 final Node
                        temp.next=ListNode(1)
                    break
            else:
                temp.next = ListNode() # Create Next Node
                if l1_current == None: # L1 is out of numbers but L2 still does, create 1 more 0 node
                    l1_current = ListNode()
                elif l2_current == None: # L2 is out of numbers but L1 still does, create 1 more 0 node
                    l2_current = ListNode()
                
            temp = temp.next
            

        return output
 
