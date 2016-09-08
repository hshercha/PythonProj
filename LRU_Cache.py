import math

'''
This project creates an LRU cache using linked lists.
'''

class Node(object):
    def __init__(self, prev=None, next=None, key=None, data=None):
        self.key = key
        self.data = data
        self.prev = prev
        self.next = next
    
    def printVal(self):
        print (self.key)
        print (self.data)

    def get_key(self):
        return self.key

    def get_data(self):
        return self.data
    
    def get_prevNode(self):
        return self.prev
    
    def get_nextNode(self):
        return self.next
    
    def set_prevNode(self, node):
        self.prev = node
    
    def set_nextNode(self, node):
        self.next = node

class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.count = 0
    
    def pushback(self, node):
        if (self.count > 1):
            if(self.head.get_key() == node.get_key()):
                """Rearrange the head"""
                nextNode = self.head.get_nextNode()
                self.head = nextNode
                self.head.set_prevNode(None)
                
                """Rearrange the tail"""
                tempTailNode = self.tail
                tempTailNode.set_nextNode(node)
                node.set_prevNode(tempTailNode)
                node.set_nextNode(None)
                self.tail = node
                
            elif(self.tail.get_key() != node.get_key()):
                
                """Rearrange the midNode"""
                tempPrevNode = node.get_prevNode()
                tempNextNode = node.get_nextNode()
                
                tempPrevNode.set_nextNode(tempNextNode)
                tempNextNode.set_prevNode(tempPrevNode)
                
                """Rearrange the tail"""
                tempTailNode = self.tail
                tempTailNode.set_nextNode(node)
                node.set_prevNode(tempTailNode)
                node.set_nextNode(None)
                self.tail = node
    
    def insert(self, node):
        if (self.count == 0):
            self.head = node
            self.head.set_nextNode(self.tail)
            self.tail = node
            self.tail.set_prevNode(self.head)
        else:
            tempTailNode = self.tail
            tempTailNode.set_nextNode(node)
            self.tail = node
            self.tail.set_prevNode(tempTailNode)
            self.tail.set_nextNode(None)
        self.count = self.count + 1
        self.printVal()
    
    def printVal(self):
        curNode = self.head
        print("Head: " + str(self.head.get_key())+ "," + str(self.head.get_data()))
        while(curNode is not None):
            print("Cur: " + str(curNode.get_key()) + "," + str(self.head.get_data()))
            curNode = curNode.get_nextNode()
        print("Tail: " + str(self.tail.get_key()) + "," + str(self.tail.get_data()))
    
    def popHead(self):
        
        if (self.count == 1):
            """Returns the head node.
            Erases the head and tail.
            """
            node = self.head
            self.head = None
            self.tail = None
            self.count = self.count - 1
            return node
        else:
            node = self.head
            nextNode = node.get_nextNode()
            if (nextNode):
                self.head = nextNode
            else:
                self.head = None
            self.count = self.count - 1
            return node
            
                
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.items = {}
        self.totalItems = 0
        self.capacity = capacity
        self.doubleList = LinkedList()

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.items:
            node = self.items[key]
            if node is None:
                return -1
            else:
                self.doubleList.pushback(node)
                return node.get_data()
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        keyExists = False
        
        if key in self.items:
            keyExists = True
        
        if keyExists == False:
            newNode = Node(prev=None, next=None, key=key, data=value)
            self.items[key] = newNode
            if (not(self.cacheIsFull())):
                self.totalItems = self.totalItems + 1
            else:
                node = self.doubleList.popHead()
                nodeKey = node.get_key()
                del self.items[nodeKey]
            self.doubleList.insert(newNode)    
        else:
            node = self.items[key]
            self.doubleList.pushback(node)
    
    def cacheIsFull(self):
        if (self.capacity == self.totalItems):
            return True
        else:
            return False

if __name__ == "__main__":
	lruCache = LRUCache(2)

	lruCache.set(2,1)
	lruCache.set(2,2)
	lruCache.get(2)
	lruCache.set(1,1)
	lruCache.set(4,1)
	lruCache.get(2)