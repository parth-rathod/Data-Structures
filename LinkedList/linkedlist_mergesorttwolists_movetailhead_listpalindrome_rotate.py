class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            
    
    def append(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return 
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    
    def merge_sort(self,llist):
        p = self.head
        q = llist.head
        s = None
        
        if not p:
            return q
        if not q:
            return p
        
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
        new = s
        
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
                
        if not p:
            s.next = q
        if not q:
            s.next = p
            
        self.head = new
        return new
        
    def move_tail_head(self):
        cur = self.head
        prev = None
        while cur.next:
            prev = cur
            cur = cur.next
        cur.next = self.head
        self.head = cur
        prev.next = None
        
    def list_palindrome(self):
        cur = self.head
        s = ''
        while cur:
            s += cur.data
            cur = cur.next
        return s == s[::-1]
        
        
    def rotate_list(self,k):
        count = 0
        cur = self.head
        last = self.head
        prev = None
        while cur and count < k:
            prev = cur
            cur = prev.next
            last = last.next
            count += 1
        cur = prev
        while last:
            prev = last
            last = last.next
        last = prev
        last.next = self.head
        self.head = cur.next 
        cur.next = None
        
        
llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append("A")
llist_1.append("B")
llist_1.append("C")
llist_1.append("D")
#llist_1.append(10)

#llist_2.append(2)
#llist_2.append(3)
#llist_2.append(4)
#llist_2.append(6)
#llist_2.append(8)

#llist_1.merge_sort(llist_2)
#llist_1.move_tail_head()
#print(llist_1.list_palindrome())
llist_1.rotate_list(3)
llist_1.print_list()
