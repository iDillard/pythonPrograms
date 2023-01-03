"""
Isaiah Dillard
09/21/2022

File: listbag.py
Author: Man-Chi Leung
"""

from node import Node

class ListBag(object):
    """A list-based bag implementation."""

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

        return len(self) == 0
    
    def __len__(self):
        """Returns the number of items in self."""

        return self.size


    def __str__(self):
        """Returns the string representation of self."""

        return "{" + ", ".join(map(str, self)) + "}"


    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self.items
        while cursor != None:
            yield cursor.data
            cursor = cursor.next

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""

        # create a instance of self and set it equal to result
        # add the items from the incoming (other) then add
        # then items add it to self.
        result = ListBag(self)
        for item in other:
            result.add(item)
        return result


    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""

        # Test to see if the incoming matches the current self
        if self is other:
            return True

        # testing the type of self against other
        #  or
        # if the types are the same test the length
        if type(self) != type(other) or len(self) != len(other):
            return False

        # compare the two items in both bags
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True


    def count(self, item):
        """Returns the number of instances of item in self."""
        # create a counter
        count = 0

        # look through the items in self and compare
        # to items to incoming item
        # if they match add to counter
        for i in self:
            if i == item:
                count += 1

        return count

    # Mutator methods
    def clear(self):
        """Makes self become empty."""

        # Reset the list and size back to empty

        self.items = list()
        self.size = 0


    def add(self, item):
        """Adds item to self."""

        self.items.append(item)
        self.size += 1


    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""

        # test if the item is in bag already
        # if the item is not return message
        if item not in self:
            raise KeyError(str(item) + " not in bag")
        else:
            self.items.remove(item)

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

        # help(ListBag)

        

