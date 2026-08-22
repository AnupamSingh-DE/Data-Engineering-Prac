import heapq

class TaskSchedular:

    def __init__(self):
        self._task_list = []

    class Task:
        def __init__(self,name,priority):
            self.name = name
            self.priority = priority

        def __repr__(self):
            return f'Name : {self.name}'

    def add_task(self,name,priority):
        task = self.Task(name,priority)
        heapq.heappush(self._task_list, (priority, task))

    def next_task(self):
        if self._task_list:
            return heapq.heappop(self._task_list)
        else:
            return None

    def peek_task(self):
        if self._task_list:
            return self._task_list[0]
        else:
            return None

            