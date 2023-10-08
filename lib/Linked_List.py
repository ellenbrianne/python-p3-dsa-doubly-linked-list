class Node:
  def __init__(self, data, next_node = None, prev_node = None):
    self.data = data
    self.next_node = next_node
    self.prev_node = prev_node


class SinglyLinkedList:
  def __init__(self, head = None, tail = None):
    self.head = head
    self.tail = tail

  def append(self, node):
    # Add element to the beginning of the list if the list is empty
    if self.head == None:
        self.head = node
        self.tail = node
        return
    # no need to traverse! we can access the last node directly (self.tail)
    # 1 -> 2 -> 3
    self.tail.next_node = node
    # 1 -> 2 -> 3 -> 4
    # we also need to make sure to keep track of the new tail

    self.tail = node

    def delete_tail(self):
      if self.head == None:
        return
      # traverse the entire list to find the second-to-last node (prev)
      curr = self.head
      prev = None
      while curr.next_node:
        prev = curr
        curr = curr.next_node
      # remove the last node by removing the link between the second-to-last node and the tail
      # 1 -> 2 -> 3
      prev.next_node = None
      # 1 -> 2

class DoublyLinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def delete_tail(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # traverse the entire list to find the second-to-last node (prev)
        else:
        # access the second-to-last node (self.tail.prev_node)
            prev = self.tail.prev_node
            # update the tail and next_node pointers
            # 1 <-> 2 <-> 3
            prev.next_node = None
            self.tail = prev
            # 1 <-> 2

    def append(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return
        node.prev_node = self.tail
        self.tail.next_node = node
        self.tail = node