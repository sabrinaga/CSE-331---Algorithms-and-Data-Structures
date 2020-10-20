class CircularQueue():
    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0


    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size

    # -----------MODIFY BELOW--------------

    def __str__(self):
        ''' :return: string representation'''
        if self.size == 0:
            return "Empty Stack"

        output = []
        for i in range(self.size):
            output.append(str(self.data[i]))
        return "{} Capacity: {}".format(output, str(self.capacity))

    def is_empty(self):
        ''':return: Bool, True if queue is empty'''
        return self.size == 0

    def __len__(self):
        ''':return: size of the queue'''
        return self.size

    def first_value(self):
        ''':return: the first value of the queue'''
        return self.data[self.head]

    def enqueue(self, val):
        ''':param val: value that needs to be added to the end of the queue'''
        if self.size == self.capacity-1:
            self.grow()
        self.tail = (self.tail + 1) % self.capacity
        self.data[self.tail -1] = val
        self.size += 1

    def dequeue(self):
        ''':return: value removed fromt he queue, if the queue is empty returns None.'''
        if self.is_empty():
            return None
        popped_val = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head +1) % self.capacity
        self.size -= 1
        if self.size == (self.capacity // 4):
            self.shrink()
        return popped_val

    def grow(self):
        '''Creates a new array to hold the queue,
        that is double the capacity of the previes queue'''
        old_cap = self.capacity
        self.capacity = self.capacity * 2
        new_arry = []
        for i in range(0, self.capacity):
            new_arry.append(None)
        for i in range(0, self.size):
            new_arry[i] = self.data[self.head]
            self.head = (self.head +1) % old_cap
        self.data = new_arry
        self.head = 0
        self.tail = self.size

    def shrink(self):
        '''Shrinks the queue to half
        if the size is a quarter of the capacity'''
        old_cap = self.capacity
        if self.capacity >= 8:
            self.capacity = self.capacity // 2
            new_arry = []
            for i in range(0, self.capacity):
                new_arry.append(None)
            for i in range(0, self.size):
                new_arry[i] = self.data[self.head]
                self.head = (self.head + 1) % old_cap
            self.data = new_arry
            self.head = 0
            self.tail = self.size
