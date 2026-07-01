from typing import Any

class Node:
    def __init__(self, val:Any):
        self.val = val
        self.next: Node | None = None
    
    def set_next(self, node: Node | None):
        self.next = node

    def __repr__(self):
        return str(self.val)

class Solution:
    def reverseList(self, head: Optional[Node]) -> Optional[Node]:
        current = head
        previous = None

        while current is not None:
            next_node = current.next

            #Reverse the pointer
            current.next = previous

            previous = current

            current = next_node

        return previous

        

             





        