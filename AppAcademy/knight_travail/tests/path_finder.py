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

finder = KnightPathFinder((0,0))
# print(finder.new_move_positions((0,0)))
finder.build_move_tree()
print(finder._root.children)