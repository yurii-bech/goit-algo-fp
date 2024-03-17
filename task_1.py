class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self, head):
        if head is None or head.next is None:
            return head
        
        middle = self.find_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.merge(left, right)
        return sorted_list

    def find_middle(self, head):
        if head is None:
            return head
        
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        
        merged = None
        if left.data <= right.data:
            merged = left
            merged.next = self.merge(left.next, right)
        else:
            merged = right
            merged.next = self.merge(left, right.next)
        return merged

def merge_sorted_lists(list1, list2):
    merged = LinkedList()
    current1 = list1.head
    current2 = list2.head

    while current1 is not None and current2 is not None:
        if current1.data <= current2.data:
            merged.append(current1.data)
            current1 = current1.next
        else:
            merged.append(current2.data)
            current2 = current2.next
    
    while current1 is not None:
        merged.append(current1.data)
        current1 = current1.next

    while current2 is not None:
        merged.append(current2.data)
        current2 = current2.next

    return merged

# Приклад використання:
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(1)
linked_list.append(2)

print("Початковий список:")
current = linked_list.head
while current is not None:
    print(current.data, end=' ')
    current = current.next
print()

# Реверсування списку
linked_list.reverse()
print("Реверсований список:")
current = linked_list.head
while current is not None:
    print(current.data, end=' ')
    current = current.next
print()

# Сортування злиттям
sorted_list = linked_list.merge_sort(linked_list.head)
print("Відсортований список:")
current = sorted_list
while current is not None:
    print(current.data, end=' ')
    current = current.next
print()

# Об'єднання відсортованих списків
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

merged_list = merge_sorted_lists(list1, list2)
print("Об'єднаний відсортований список:")
current = merged_list.head
while current is not None:
    print(current.data, end=' ')
    current = current.next
print()