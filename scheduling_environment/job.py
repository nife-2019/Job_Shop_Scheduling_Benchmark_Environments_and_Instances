from typing import List
from scheduling_environment.operation import Operation


class Job:
    def __init__(self, job_id: int):
        self._job_id: int = job_id
        self._operations: List[Operation] = []
        self._arrival_time: int = 0  # 添加作业到达时间
        self._due_date: int = 0  # 添加作业交期

    @property
    def arrival_time(self) -> int:
        """Return the job's arrival time."""
        return self._arrival_time
    def set_arrival_time(self, arrival_time: int) -> None:
        self._arrival_time = arrival_time
    @property
    def due_date(self) -> int:
        """Return the job's due date."""
        return self._due_date
    def set_due_date(self, due_date: int) -> None:
        self._due_date = due_date
    @property
    def lateness(self) -> int:
        """Return the job's lateness."""
        return max(0, self.next_ope_earliest_begin_time - self.due_date)

    def add_operation(self, operation: Operation):
        """Add an operation to the job."""
        self._operations.append(operation)

    @property
    def nr_of_ops(self) -> int:
        """Return the number of jobs."""
        return len(self._operations)

    @property
    def operations(self) -> List[Operation]:
        """Return the list of operations."""
        return self._operations

    @property
    def job_id(self) -> int:
        """Return the job's id."""
        return self._job_id

    @property
    def scheduled_operations(self) -> List[Operation]:
        """Return a list of operations that have been scheduled to a machine."""
        return [operation for operation in self._operations if operation.scheduling_information != {}]

    @property
    def next_ope_earliest_begin_time(self):
        """Returns the time at which all operations currently scheduled for this job have finished processing."""
        return max([operation.scheduled_end_time for operation in self.scheduled_operations], default=0)

    def get_operation(self, operation_id):
        """Return operation object with operation id."""
        for operation in self._operations:
            if operation.operation_id == operation_id:
                return operation
