class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
class CircularLinklist():
    def __init__(self):
        self.head = None
        
    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
            
    def prepend(self,data):
        new_node = Node(data)
        cur = self.head 
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node
        
    def printlist(self):
        if self.head is None:
            return "No node in List"
        else:
            cur = self.head
            while cur:
                print(cur.data)
                cur = cur.next
                if cur == self.head:
                    break
                
    def remove(self,key):
        if self.head.next == self.head and self.head.data == key:
            self.head = None
            return
        if self.head.data == key:
            cur = self.head 
            while cur.next != self.head:
                cur = cur.next 
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head 
            prev = None 
            while cur.next != self.head:
                prev = cur 
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next 
                    cur = cur.next
                    
                    
    def __len__(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count
    
    def split(self):
        size = len(self)
        
        if size == 0:
            return "There is no node"
        if size == 1:
            return "There is only 1 Node"
        
        cut = size // 2
        cur = self.head
        count = 0
        prev = None
        while cur and count < cut:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head
        
        secondlist = CircularLinklist()
        while cur.next != self.head:
            secondlist.append(cur.data)
            cur = cur.next
        secondlist.append(cur.data)
        
        self.printlist()
        print("\n")
        secondlist.printlist()
        
        
    def remove_josephus(self,node):
        if self.head.next == self.head and self.head == node:
            self.head = None
            return
        if self.head == node:
            cur = self.head 
            while cur.next != self.head:
                cur = cur.next 
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head 
            prev = None 
            while cur.next != self.head:
                prev = cur 
                cur = cur.next
                if cur == node:
                    prev.next = cur.next 
                    cur = cur.next
        
    def josephus(self,step):
        cur = self.head
        
        while len(self) > 1:
            count = 1
            while count != step:
                count += 1
                cur = cur.next
                print("Node Removed:", cur.data)
            self.remove_josephus(cur)
            cur = cur.next
            
      
    def is_circular(self,check):
        cur = check.head
        while cur:
            cur = cur.next
            if cur.next == check.head:
                return "It is Circular Link List"
        return "Not a circular Linklist"
    
    
    
    
            
            
clist = CircularLinklist()
clist.append("A")
clist.append("B")
clist.append("C")
clist.append("D")

#clist.remove("A")
#clist.remove("C")
#clist.josephus(2)
#clist.split()
#clist.printlist()
clist.is_circular(clist)           
