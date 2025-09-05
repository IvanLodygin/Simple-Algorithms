import math

def calculate_optimal_node_size(num_elements):
    cache_size = 64
    int_size = 4
    memory_size = num_elements*int_size
    optimal_node_size = math.ceil(memory_size/cache_size) + 1
    return optimal_node_size

class Node:
    def __init__(self, node_size, node_num):
        self.elements = list()
        self.node_size = node_size
        self.node_num = node_num
        self.next = None
        
class UnrolledLinkedList:
    def __init__(self, elements):
        self.element_nums = len(elements)
        self.node_size = calculate_optimal_node_size(self.element_nums)
        self.head = Node(self.node_size, 0)
        self.node_nums = 1
        counter = 0
        
        for element in elements:
            counter += 1
            current_node = self.head
            while(True):
                if(current_node.next is None):
                    break
                current_node = current_node.next
            current_node.elements.append(element)
            if(len(current_node.elements) == self.node_size):
                if(counter == self.element_nums):
                    current_node.next = None
                else:
                    current_node.next = Node(self.node_size, current_node.node_num + 1)
                    self.node_nums += 1
                
    def recreate_list(self, elements):
        self.element_nums = len(elements)
        self.node_size = calculate_optimal_node_size(self.element_nums)
        self.head = Node(self.node_size, 0)
        self.node_nums = 1
        counter = 0
        
        for element in elements:
            counter += 1
            current_node = self.head
            while(True):
                if(current_node.next is None):
                    break
                current_node = current_node.next
            current_node.elements.append(element)
            if(len(current_node.elements) == self.node_size):
                if(counter == self.element_nums):
                    current_node.next = None
                else:
                    current_node.next = Node(self.node_size, current_node.node_num + 1)
                    self.node_nums += 1
        
    
    def push_back(self, node_element):
        if(calculate_optimal_node_size(self.element_nums + 1) != self.node_size):
            elements = self.get_elements_list()
            elements.append(node_element)
            self.recreate_list(elements)
            return
        
        current_node = self.head

        while(True):
            if(current_node.next) == None:
                break
            current_node = current_node.next

        if(len(current_node.elements) == self.node_size):
            current_node.next = Node(self.node_size, current_node.node_num + 1)
            current_node = current_node.next
            self.node_nums += 1

        current_node.elements.append(node_element)
        self.element_nums += 1
            
    def insert_element(self, index, node_element):
        if(index >= self.__len__() or index < 0):
            raise IndexError('list index out of range')
        
        if(calculate_optimal_node_size(self.element_nums + 1) != self.node_size):
            elements = self.get_elements_list()
            elements.insert(index, node_element)
            self.recreate_list(elements)
            return
        
        self.element_nums += 1
        node_num = int(index/self.node_size)
        target_node = self.head

        for _ in range(node_num):
            target_node = target_node.next

        target_node.elements.insert(index % self.node_size, node_element)
        
        if(len(target_node.elements) > self.node_size):
            deleted_element = target_node.elements.pop()
        else: return

        if(target_node.next is None):
            self.push_back(deleted_element)
            return
        
        while(True):
            target_node = target_node.next
            if(target_node.next is None):
                if(len(target_node.elements) >= self.node_size):
                    target_node.elements.insert(0, deleted_element)
                    deleted_element = target_node.elements.pop()
                self.push_back(deleted_element)
                return
            else:
                target_node.elements.insert(0, deleted_element)
                deleted_element = target_node.elements.pop()
                
    def push_forward(self, node_element):
        if(calculate_optimal_node_size(self.element_nums + 1) != self.node_size):
            elements = self.get_elements_list()
            elements.insert(0, node_element)
            self.recreate_list(elements)
            return
        self.insert_element(0, node_element)
                 
    def delete_element(self, node_element):
        element_index = self.find_element(node_element)

        if(element_index is None):
            return
        else: element_index = element_index['index']

        if(calculate_optimal_node_size(self.element_nums - 1) != self.node_size):
            elements = self.get_elements_list()
            elements.pop(element_index)
            self.recreate_list(elements)
            return node_element
        
        node_num = int(element_index/self.node_size)
        target_node = self.head
        for _ in range(node_num):
            target_node = target_node.next
        target_node.elements.remove(node_element)
        self.element_nums -= 1

        while(True):
            if(target_node.next is None):
                if(not target_node.elements):
                    self.node_nums -= 1
                    target_node = None
                return node_element
            target_node.elements.append(target_node.next.elements[0])

            if(len(target_node.next.elements) == 1):
                self.node_nums -= 1
                target_node.next = None
                return node_element
            else:
                target_node.next.elements.pop(0)
                target_node = target_node.next

    def find_element(self, element):
        current_node = self.head
        while(True):
            if element in current_node.elements:
                return {'position': f'Node: {current_node.node_num}, node index: {current_node.elements.index(element)}',
                        'index': current_node.node_num*self.node_size + current_node.elements.index(element)}
            if(current_node.next is None): return None
            current_node = current_node.next
            
    def get_elements_list(self):
        elements = list()
        current_node = self.head
        while(True):
            elements += current_node.elements
            if(current_node.next is None): break
            current_node = current_node.next
        return elements
            
    def __len__(self):
        lenght = 0
        current_node = self.head
        while(True):
            lenght += len(current_node.elements)
            if(current_node.next is None): break
            current_node = current_node.next
        return lenght
            
    def __str__(self):
        current_node = self.head
        res = ''
        while(True):
            if(current_node.elements):
                res+=f'Node {current_node.node_num}: ' + ' '.join([str(element) for element in current_node.elements]) + '\n'
            if(current_node.next is None): break
            current_node = current_node.next
        return res

def check(arr_1, arr_2):
    my_list = UnrolledLinkedList([])
    for el in arr_1:
        my_list.push_back(el)
        print(my_list)
    for el in arr_2:
        my_list.delete_element(el)
        print(my_list)

elements = list(map(int, input().split()))
my_list = UnrolledLinkedList(elements)
print(my_list, end='')