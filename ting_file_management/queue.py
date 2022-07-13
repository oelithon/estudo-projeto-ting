class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        return self._data.append(value)

    def dequeue(self):
        value = self._data[0]
        del self._data[0]
        return value

    def search(self, index):
        if index < 0 or index > (len(self._data)-1):
            raise IndexError
        value = self._data[index]
        return value
