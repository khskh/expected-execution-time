import time
import random
from CalculateExpectedTime import CalculateExpectedTime

if __name__ == "__main__":
    # Define the number of loop iterations
    required_number_of_loop_iterations = 10

    # Create an instance of CalculateExpectedTime
    time_calculation = CalculateExpectedTime(required_number_of_loop_iterations)

    for i in range(required_number_of_loop_iterations):
        time_calculation.start()

        # your code
        delay = random.uniform(2, 4)
        print(f'\nIteration {i + 1}: Waiting for {delay:.2f} seconds...\n')
        time.sleep(delay)
        # your code

        time_calculation.stop()
        time_calculation.print_statistics()

        """ or use:
        print(time_calculation.execution_time)
        print(time_calculation.actual_iteration_time)
        print(time_calculation.average_iteration_time)
        print(time_calculation.percentage_of_program_completion)
        print(time_calculation.expected_duration_of_the_program)
        print(time_calculation.estimated_time_until_the_end_of_the_program)
        """

    time_calculation.reset()

