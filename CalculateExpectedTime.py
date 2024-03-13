import datetime


class CalculateExpectedTime:
    def __init__(self, number_of_iterations):
        """
        Initialize the object to calculate the expected program execution time.

        :param number_of_iterations: Number of iterations in the program.
        """
        if not isinstance(number_of_iterations, int):
            raise ValueError("Number of iterations must be an integer")
        self.number_of_iterations = number_of_iterations

        self.current_iteration = 0
        self.total_execution_time = 0

        self.iteration_start_time = None
        self.iteration_stop_time = None
        self.iteration_time = None

        self.started = False

    def reset(self):
        """
        Reset the counters.

        :return: None
        """
        self.current_iteration = 0
        self.total_execution_time = 0
        self.started = False

    def start(self) -> None:
        """
        Start measuring the iteration time.

        :return: None
        """
        if self.started:
            raise RuntimeError("start() has already been called")

        self.iteration_start_time = datetime.datetime.now()
        self.current_iteration += 1
        self.started = True

    def stop(self) -> None:
        """
        Stop measuring the iteration time.

        :return: None
        """
        if not self.started:
            raise RuntimeError("start() must be called first")

        self.iteration_stop_time = datetime.datetime.now()
        self.iteration_time = self.iteration_stop_time - self.iteration_start_time
        self.total_execution_time += self.iteration_time.total_seconds()
        self.started = False

    @property
    def execution_time(self):
        """
        Returns the total execution time of the program.

        :return: Total execution time
        """
        return self.total_execution_time

    @property
    def actual_iteration_time(self) -> float:
        """
        Returns the time of the last iteration in seconds.

        :return: Iteration time in seconds
        """
        return self.iteration_time.total_seconds()

    @property
    def average_iteration_time(self) -> float:
        """
        Returns the average time of one iteration in seconds.

        :return: Average iteration time in seconds
        """
        return self.total_execution_time / self.current_iteration

    @property
    def percentage_of_program_completion(self) -> str:
        """
        Returns the percentage of program completion.

        :return: Program execution in percent
        """
        return "{:.2f} %".format((self.current_iteration / self.number_of_iterations) * 100)

    @property
    def expected_duration_of_the_program(self) -> float:
        """
        Returns the expected completion time of the program.

        :return: Expected completion time
        """
        return self.average_iteration_time * self.number_of_iterations

    @property
    def estimated_time_until_the_end_of_the_program(self) -> float:
        """
        Returns the estimated time until the end of the program.

        :return: Expected time until the end of the program
        """
        return (self.average_iteration_time * self.number_of_iterations) - self.total_execution_time

    def print_statistics(self) -> None:
        """
        Displays all program statistics.

        :return: None
        """
        print("Program execution time:", self.execution_time)
        print("Iteration time:", self.actual_iteration_time)
        print("Average iteration time:", self.average_iteration_time)
        print("Program completion percentage:", self.percentage_of_program_completion)
        print("Expected program execution time:", self.expected_duration_of_the_program)
        print("Estimated time until the end of the program:", self.estimated_time_until_the_end_of_the_program)
