class TreeNode:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.node_height = 1

def compute_height(node: TreeNode) -> int:
    return 0 if node is None else node.node_height

def get_balance(node: TreeNode) -> int:
    return compute_height(node.right_child) - compute_height(node.left_child)

def refresh_height(node: TreeNode):
    left_height = compute_height(node.left_child)
    right_height = compute_height(node.right_child)
    node.node_height = max(left_height, right_height) + 1

def rotate_right(node: TreeNode) -> TreeNode:
    pivot = node.left_child
    node.left_child = pivot.right_child
    pivot.right_child = node
    refresh_height(node)
    refresh_height(pivot)
    return pivot

def rotate_left(node: TreeNode) -> TreeNode:
    pivot = node.right_child
    node.right_child = pivot.left_child
    pivot.left_child = node
    refresh_height(node)
    refresh_height(pivot)
    return pivot

def rebalance(node: TreeNode) -> TreeNode:
    refresh_height(node)
    balance = get_balance(node)
    
    if balance < -1:
        if get_balance(node.left_child) > 0:
            node.left_child = rotate_left(node.left_child)
        return rotate_right(node)
    
    if balance > 1:
        if get_balance(node.right_child) < 0:
            node.right_child = rotate_right(node.right_child)
        return rotate_left(node)

    return node

def insert_value(value: int, node: TreeNode) -> TreeNode:
    stack = []
    current = node
    while current:
        stack.append(current)
        if value < current.value:
            if current.left_child is None:
                current.left_child = TreeNode(value)
                break
            current = current.left_child
        else:
            if current.right_child is None:
                current.right_child = TreeNode(value)
                break
            current = current.right_child
    
    if not stack:
        return TreeNode(value)
    
    while stack:
        current = stack.pop()
        current = rebalance(current)
    
    return current

def find_min(node: TreeNode) -> TreeNode:
    while node.left_child:
        node = node.left_child
    return node

def delete_max(node: TreeNode) -> TreeNode:
    parent, current = None, node
    while current.right_child:
        parent, current = current, current.right_child
    if parent:
        parent.right_child = current.left_child
        return rebalance(node)
    else:
        return current.left_child

def delete_min(node: TreeNode) -> TreeNode:
    parent, current = None, node
    while current.left_child:
        parent, current = current, current.left_child
    if parent:
        parent.left_child = current.right_child
        return rebalance(node)
    else:
        return current.right_child

def delete_value(value: int, node: TreeNode) -> TreeNode:
    parent = None
    current = node
    
    while current and current.value != value:
        parent = current
        if value < current.value:
            current = current.left_child
        else:
            current = current.right_child
    
    if current is None:
        return node
    
    if current.left_child and current.right_child:
        min_larger_node = find_min(current.right_child)
        current.value = min_larger_node.value
        current.right_child = delete_min(current.right_child)
    elif current.left_child or current.right_child:
        child = current.left_child if current.left_child else current.right_child
        if parent is None:
            return child
        if parent.left_child == current:
            parent.left_child = child
        else:
            parent.right_child = child
    else:
        if parent is None:
            return None
        if parent.left_child == current:
            parent.left_child = None
        else:
            parent.right_child = None

    return rebalance(node)

def calculate_height(node: TreeNode) -> int:
    stack = [(node, 1)]
    max_height = 0
    while stack:
        node, height = stack.pop()
        if node is not None:
            max_height = max(max_height, height)
            stack.append((node.left_child, height + 1))
            stack.append((node.right_child, height + 1))
    return max_height

def is_balanced(node: TreeNode) -> bool:
    if node is None:
        return True
    
    left_height = calculate_height(node.left_child)
    right_height = calculate_height(node.right_child)
    
    if abs(left_height - right_height) > 1:
        return False
    
    return is_balanced(node.left_child) and is_balanced(node.right_child)

def print_tree(node: TreeNode, level=0):
    if node is not None:
        print_tree(node.right_child, level + 1)
        print(' ' * 4 * level + '->', node.value)
        print_tree(node.left_child, level + 1)