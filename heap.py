import math

BASE_FOR_LOG = 2


class Heap:
    def __init__(self, array):
        self.array = array

    def __repr__(self):
        return str(self.array)

    def append_new_element(self, new_element, sort_new_element=True):
        """this method append new item in the last of array,it's means that element considering disordered,
        so argument sort_new_element allow to sort array in needed order thanks for method action_up """
        self.array.append(new_element)
        if sort_new_element:
            self.action_up(len(self.array))

    def action_up(self, index):
        """this method to move element with getting index on right place  """
        while index > 1:
            # sibling_index allow to check availability right element for left element and to know how is less of them
            # so adding sibling_index to main index indicates which element will be move up
            sibling_index = 0
            try:
                # if left element doesn't contain sibling element then block try processing IndexError
                if self.array[index - 1] > self.array[index]:
                    sibling_index = 1
            except IndexError:
                pass
            # in this case occurs moving up element on correct place
            if self.array[index - 1 + sibling_index] < self.array[index // 2 - 1]:
                change_element = self.array[index // 2 - 1]
                self.array[index // 2 - 1] = self.array[index - 1 + sibling_index]
                self.array[index - 1 + sibling_index] = change_element
            index //= 2

    def check_order_array(self):
        """this method has checked array on order"""
        return self.array == sorted(self.array)

    def check_order_heap(self):
        """this method check has checked heap on order(not array!!!)"""
        bool_values = True
        for target_index in range(len(self.array)):

            try:
                if self.array[target_index] > self.array[2 * target_index + 1] or \
                        self.array[target_index] > self.array[2 * target_index + 2]:
                    bool_values = False
                    break
            except IndexError:
                break
        return bool_values

    def extract_min_element(self):
        """this method allows to extract least """
        if not self.check_order_array():
            self.heap_sort()
        return self.array.pop(0)

    def heap_sort(self):
        """this method represents heap sort with creating new ordered array """
        new_heap = []
        # this circle passing each element in array
        for index in range(len(self.array), 0, -1):
            # this circle passing on each level in heap
            for level_index in range(self.get_heap_len(), 0, -1):
                target_index = 0
                target_element = pow(2, level_index)
                # this circle passing thought even elements which allows on target level
                while target_index < target_element and target_element + target_index <= index:
                    self.action_up(target_element + target_index)
                    target_index += 2

            # in this case occurs replacing least element after permutations on first position
            # and last element in array,after this action last element has deleted and added in new array
            change_element = self.array[index - 1]
            self.array[index - 1] = self.array[0]
            self.array[0] = change_element
            new_heap.append(self.array.pop())

        self.array = new_heap

    def get_heap_len(self):
        """" this method return heap_len start with 0 for example:[1,2,3]->1 or [1,2,3,4]->2 """
        return int(math.log(len(self.array), BASE_FOR_LOG))
