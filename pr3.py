
class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def _heapify_down(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def build_heap(self, array):
        self.heap = array[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def get_heap(self):
        return self.heap


if __name__ == "__main__":
    h = Heap()
    
    # Вставка элементов
    h.insert(10)
    h.insert(20)
    h.insert(5)
    h.insert(30)
    
    print("Куча после вставки:", h.get_heap())
    
    # Извлечение максимального элемента
    max_elem = h.extract_max()
    print("Извлеченный максимальный элемент:", max_elem)
    
    print("Куча после извлечения максимального элемента:", h.get_heap())
    
    # Построение кучи из массива
    array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    h.build_heap(array)
    print("Куча из массива:", h.get_heap())