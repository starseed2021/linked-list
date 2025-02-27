
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
      self.head = None # keep the head private. Not accessible outside this class
    #   self.tail = None 

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if self.head == None:
            return None
        
        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):

        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node


    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: ?
    # Space Complexity: ?
    def search(self, value):
        if self.head == None:
            return False

        # true if head has a value
        current = self.head
        # if current == None:
        #     return False
        while current != None:
            # if the current node's value is not equal to the value parameter
            if current.value != value:
                current = current.next
            else:
                return True
        return False
                

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        current = self.head
        
        node_count = 0

        while current:
            node_count += 1
            current = current.next
        return node_count
        
    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        current = self.head

        node_count = 0

        while current:
            if node_count == index:
                return current.value
            node_count += 1
            current = current.next


    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def get_last(self):
        if self.head == None:
            return None
        
        current = self.head
        next_node = current.next
        while next_node != None:
            current = next_node
            next_node = current.next
        
        return current.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def add_last(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return self.head

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        return new_node


    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity 
    # Space Complexity
    def find_max(self):
        if self.head == None:
            return None

        current = self.head
        max_value = current.value
        
        while current != None:
            if current.value > max_value:
                max_value = current.value
            current = current.next
            
        return max_value


    # method to delete the first node found with specified value
    # Time Complexity: Flag O(1) ; If & Else O(n)
    # Space Complexity: O(n)
    def delete(self, value):
        if self.head == None:
            return None
        
        current = self.head

        while current != None:
            if current.value == value:
                # EX: 2-4-6-8 ; head will be 4 & LL: 4-6-8
                # reassigning the head before removal and access to it
                if current == self.head:
                    self.head = current.next
                # swapping and deleting
                current = current.next
            elif current.next.value == value:  
                # handles the removal for 4-6-8 ; EX: 2-4-6-8
                # if the next node in list != None
                # removing from the middle
                current.next = current.next.next
                current = current.next
            else:
                current = current.next
                current.next = current.next.next
 
            return current

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        if self.head == None:
            return None

        prev_node = None
        current = self.head

        while current != None:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        self.head = prev_node
        return self.head
  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def find_middle_value(self):
        pass

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        pass

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        pass

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node
