from stack import Stack


def test_constructor_is_no_arg():
    Stack()


def test_new_stack_has_zero_elements():
    assert len(Stack()) == 0


def test_push_increase_length_by_one():
    s = Stack()
    s.push(None)
    assert len(s) == 1


def test_peek_return_last_item_pushed_but_leaves_it_on_stack():
    s = Stack()
    s.push(7)
    assert s.peek() == 7
    assert len(s) == 1


def test_pop_return_last_item_pushed_and_removes_it_on_stack():
    s = Stack()
    s.push(7)
    assert s.pop() == 7
    assert len(s) == 0


def test_push_lots_of_items_makes_the_length_large():
    s = Stack()
    for i in range(1000):
        s.push(i)
    assert len(s) == 1000
    

def test_pop_lots_of_values_makes_the_length_decrease():
    s = Stack()
    for i in range(100):
        s.push(i)
    for i in range(10):
        s.pop()
    assert len(s) == 90
    assert s.peek() == 89