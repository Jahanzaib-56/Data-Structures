import ctypes

class DynamicArray:

    def __init__(self):
        self.size = 1
        self.n = 0
        self.arr = self.__make_array(self.size)
    
    # Returns the number of elements in the list
    def __len__(self):
        return self.n

    # Returns a string representation of the list
    def __str__(self):
        
        result = ''
        for i in range(self.n):
            result = result + str(self.arr[i]) + ','

        return '[' + result[:-1] + ']'
    
    # Returns the element at the given index
    def __getitem__(self, index):

        if isinstance(index, int):
            if index < 0:
                index = self.n + index
            
            if 0 <= index < self.n:
                return self.arr[index]
            else:
                raise IndexError('Index out of range')
        
        elif isinstance(index, slice):
            # Handle slicing
            start, stop, step = index.indices(self.n)
            
            new_list = MyList()
            for i in range(start, stop, step):
                new_list.append(self.arr[i])
            return new_list
        else:
            raise TypeError("List indices must be integers or slices, not {}".format(type(index).__name__))
        
    # Removes the element at the given index
    def __delitem__(self, pos):
        
        if 0 <= pos < self.n:

            for i in range(pos, self.n - 1):
                self.arr[i] = self.arr[i + 1]

            self.n = self.n - 1

        else:

            return 'Index Error'

    def __setitem__(self, index, value):

        if 0 <= index < self.n:
            self.arr[index] = value
        else:
            raise IndexError('Index out of range')  

    # Adds an element to the end of the list    
    def append(self, item):

        if self.n == self.size:
            self.__resize(self.size*2)

        self.arr[self.n] = item
        self.n = self.n + 1

    # Removes and returns the last element of the list  
    def pop(self):

        if self.n == 0:
            return "IndexError: Can't pop from empty list"
        
        print(self.arr[self.n-1])
        self.n = self.n - 1

    # Removes all elements from the list
    def clear(self):
        self.n = 0
        self.size = 1

    # Returns the index of the first occurrence of the given element
    def find(self, item):

        for i in range(self.n):
            if self.arr[i] == item:
                return i

        return f'Value Error: {item} is not in List'

    # Inserts an element at the given index
    def insert(self, pos, item):

        if 0 <= pos < self.n:

            if self.n == self.size:
                self.__resize(self.size*2)
            for i in range(self.n, pos, -1):
                self.arr[i] = self.arr[i-1]
            self.arr[pos] = item
            self.n = self.n + 1
            
        else:
            return 'IndexError'
        
    # Removes the first occurrence of the given element
    def remove(self, item):
        
        pos = self.find(item)

        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos

    # Appends all elements of another list to this list
    def extend(self, other):

        for i in other:
            self.append(i)

    # Returns the minimum element in the list
    def min(self):

        min = self.arr[0]

        for i in range(1, self.n):
            if self.arr[i] < min:
                min = self.arr[i]

        return min

    # Returns the maximum element in the list
    def max(self):

        max = self.arr[0]

        for i in range(1, self.n):
            if self.arr[i] > max:
                max = self.arr[i]

        return max

    # Returns the sum of all elements in the list
    def sum(self):

        sum = 0

        for i in range(self.n):
            sum = sum + self.arr[i]

        return sum

    # Sorts the list in ascending order
    def sort(self):

        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.arr[i] > self.arr[j]:
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    # Reverses the list in place
    def reverse(self):

        for i in range(self.n//2):
            self.arr[i], self.arr[self.n-i-1] = self.arr[self.n-i-1], self.arr[i]

    # Resizes the internal array to the given capacity
    def __resize(self, new_cap):
        new_arr = self.__make_array(new_cap)
        self.size = new_cap

        for i in range(self.n):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    # Creates a new array with the given capacity
    def __make_array(self, capacity):
        return (capacity * ctypes.py_object)()
        

# Creating a List object
List = DynamicArray()

# Appending elements to the list    
List.append(10)
List.append(20)
List.append(30)
print("List after appends:", List)

# Inserting an element at a specific index
List.insert(1, 15)
print("List after insert at index 1:", List)

# Setting an element at a specific index
List[0] = 5
print("List after setting index 0 to 5:", List)

# Accessing an element at a specific index
print("Element at index 2:", List[2])

# Removing the last element from the list
List.pop()
print("List after pop:", List)

# Removing the first occurrence of a specific element
List.remove(1)
print("List after deleting element at index 1:", List)

# Appending more elements to the list
List.append(40)
List.append(5)
print("List before sort:", List)

# Sorting the list
List.sort()
print("List after sort:", List)

# Reversing the list
List.reverse()
print("List after reverse:", List)

# Printing the sum of elements in the list
print("Sum of elements:", List.sum())
