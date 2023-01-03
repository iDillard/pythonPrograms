"""
Isaiah Dillard
09/22/2022
File: listset.py
"""
from node import Node

class ListSet(object):
    """A list-based set implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = list()
        self.size = 0

        if sourceCollection:
            for item in sourceCollection:
                self.add(item)



    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""

        # looks to see if the size is equal to zero
        # meaning there is nothing in there
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in self."""
        # Looks at size of the list and returns the number of items
        return self.size

    def __str__(self):
        """Returns the string representation of self."""

        return '{' + ','.join(map(str, self)) + '}'

    def __iter__(self):
        """Supports iteration over a view of self."""

        position = self.items

        # read what is in that position
        # return the data
        # then move to the next item
        while position != None:
            yield position.data
            position = position.next

    def __add__(self, other):
        """Returns a new set containing the contents
        of self and other."""

        bag = ListSet(self)



        # copy item from other in bag
        for item in other:
            if item in bag:
                continue
            else:
                bag.add(item)

        return bag

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""

        if self is other:
            return True

        # Test to make sure that the type and  length are the same
        if type(self) != type(other) or len(self) != len(other):
            return False
        else:
            return True

        # Compare the items within the two

    # Mutator methods
    def clear(self):
        """Makes self become empty."""

        self.items = None
        self.size = 0

    def add(self, item):
        """Adds item to self."""
        if item not in self.items:
            self.items.append(item)


    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""

        # test if item is in self
        if item not in self:
            raise KeyError(str(item) + ' not in list')

        probe = self.items
        trailer = None

        for target in self:
            if target == item:
                break
            trailer = probe
            probe = probe.next

        if probe == self.items:
            self.items = self.items.next
        else:
            trailer.next = probe.next

        self.size -= 1



