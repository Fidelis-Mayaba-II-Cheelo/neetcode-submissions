from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()

    def extensions(self, items):
        for item in items:
            self.enqueue(item)

    def enqueue(self, item: int):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return 0
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            return 0
        return self.items[0]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        tickets_queue = Queue()
        
        # Store [original_index, ticket_count]
        paired_tickets = [[i, ticket] for i, ticket in enumerate(tickets)]
        tickets_queue.extensions(paired_tickets)
        
        while not tickets_queue.is_empty():
            # 1. Get the person at the front
            current_person = tickets_queue.dequeue()
            idx = current_person[0]
            tickets_left = current_person[1]
            
            # 2. Buy a ticket
            tickets_left -= 1
            count += 1
            
            # 3. Check if it was person k's last ticket
            if idx == k and tickets_left == 0:
                return count
                
            # 4. If they still need tickets, send them to the back
            if tickets_left > 0:
                tickets_queue.enqueue([idx, tickets_left])
                
        return count 
