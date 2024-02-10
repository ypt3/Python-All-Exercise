from tree import Node

class KnightPathFinder:
    def __init__(self, initial_position) -> None:
        self._root = Node(initial_position)
        self._considered_positions = {initial_position}

    def get_valid_moves(self, pos):
        x, y = pos
        possible_moves = [
            (x+2, y+1), (x+1, y+2),
            (x-1, y+2), (x-2, y+1),
            (x-2, y-1), (x-1, y-2),
            (x+1, y-2), (x+2, y-1)
        ]
        return {(x, y) for x, y in possible_moves if 0 <= x < 8 and 0 <= y < 8}
    
    def new_move_positions(self, pos):
        valid_moves = self.get_valid_moves(pos)
        new_moves = valid_moves - self._considered_positions
        self._considered_positions.update(new_moves)
        return new_moves
    
    def build_move_tree(self):
        queue = [self._root]

        while queue:
            current_node = queue.pop(0)

            # Get valid moves for the current node's position
            new_moves = self.new_move_positions(current_node.value)

            # Create child nodes for each new move and add them to the tree
            for move in new_moves:
                child_node = Node(move)
                current_node.add_child(child_node)
                queue.append(child_node) # Enqueue the child node for further exploration

    def find_path(self, end_position):
        # Use breadth_search on the root node
        end_node = self._root.breadth_search(end_position) 
        if end_node is None:
            return None # If end_position is not found, return None
        return self.trace_to_root(end_node)
    
    def trace_to_root(self, end_node):
        path = []
        current_node = end_node

        while current_node is not None:
            # Insert at the beginning to maintain the correct order
            path.insert(0, current_node.value)
            current_node = current_node.parent
        
        return path


finder = KnightPathFinder((0,0))
# print(finder.new_move_positions((0,0)))
finder.build_move_tree()
print(finder._root.children)
finder.build_move_tree()
print(finder.find_path((2, 1)))  # Expected outcome: [(0, 0), (2, 1)]
print(finder.find_path((3, 3)))  # Expected outcome: [(0, 0), (2, 1), (3, 3)]
print(finder.find_path((6, 2)))  # Expected outcome: [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
print(finder.find_path((7, 6)))  # Expected outcome: [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]
