# Calculate Expected Time

A Python class for calculating the expected execution time of a program.

## Installation

This library does not require any additional installation. Simply include the `CalculateExpectedTime`
class with these libraries in your project.

```python
import time
import random
import datetime
from CalculateExpectedTime import CalculateExpectedTime
```
## Example Usage:

```python
# Define the number of loop iterations
required_number_of_loop_iterations = 10

# Create an instance of CalculateExpectedTime
time_calculation = CalculateExpectedTime(required_number_of_loop_iterations)

for i in range(required_number_of_loop_iterations):
    time_calculation.start()

    # your code doing something
    delay = random.uniform(2, 4)
    print(f'\nIteration {i + 1}: Waiting for {delay:.2f} seconds...\n')
    time.sleep(delay)
    # your code doing something

    time_calculation.stop()
    time_calculation.print_statistics()

time_calculation.reset()
```

You can also directly display one of several parameters returned by the function, for example
```python
for i in range(required_number_of_loop_iterations):
    time_calculation.start()

    # your code doing something
    delay = random.uniform(2, 4)
    print(f'\nIteration {i + 1}: Waiting for {delay:.2f} seconds...\n')
    time.sleep(delay)
    # your code doing something

    time_calculation.stop()

    # Display different parameters

    print(time_calculation.execution_time)
    print(time_calculation.actual_iteration_time)
    print(time_calculation.average_iteration_time)
    print(time_calculation.percentage_of_program_completion)
    print(time_calculation.expected_duration_of_the_program)
    print(time_calculation.estimated_time_until_the_end_of_the_program)
    
time_calculation.reset()
```