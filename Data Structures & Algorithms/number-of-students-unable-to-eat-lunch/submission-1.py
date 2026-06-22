class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_stack = Stack()
        sandwiches_stack = Stack()
        students_stack.extend(students[::-1])
        sandwiches_stack.extend(sandwiches[::-1])

        rotations = 0

        while sandwiches_stack.size() > 0 and rotations < students_stack.size():
            if students_stack.peek() == sandwiches_stack.peek():
                students_stack.pop()
                sandwiches_stack.pop()
                rotations = 0
            else:
                students_stack.add_to_back(students_stack.pop())  
                rotations += 1
        return students_stack.size()
                    

class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item: int) -> None:
        self.items.append(item)

    #Custom method: Haven't yet learned queues
    def add_to_back(self, item: int) -> None:
        self.items.insert(0, item)

    def extend(self, items: List) -> None:
        self.items.extend(items)

    def peek(self) -> int | None:
        if self.is_empty():
            return None
        return self.items[-1]

    def pop(self) -> int | None:
        if self.is_empty():
            return None
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return len(self.items) == 0