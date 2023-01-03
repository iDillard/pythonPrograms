"""
File: listqueue.py
Author: Man-Chi Leung
"""


class ListQueue(object):
    """An list-based stack implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = []
        self.size = 0

        if sourceCollection:
            for item in sourceCollection:
                self.items.append(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if the queue is empty, or False otherwise."""
        return len(self) == 0
    
    def __len__(self):
        """Returns the number of items in the queue."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of the queue."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of the queue."""
        cursor = 0

        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new queue containing the contents
        of self and other."""

        result = ListQueue(self)

        for item in other:
            result.add(item)

        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False

        cloneSelf = ListQueue(self)
        cloneOther = other

        for i in cloneSelf:
            for j in cloneOther:
                if cloneSelf.pop() != cloneOther.pop():
                    return False
        return True

    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises IndexError if queue is empty."""

        if self.items:
            return self.items[0]
        else:
            raise IndexError

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items = []
        self.size = 0

    def add(self, item):
        """Inserts item at rear of the queue."""
        self.items.append(item)
        self.size += 1

    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises IndexError if queue is not empty.
        Postcondition: the front item is removed from the queue."""

        if self.items:
            self.size -= 1
            return self.items.pop(0)
        else:
            raise IndexError
