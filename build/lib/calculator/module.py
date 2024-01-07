import doctest


class CalculatorClass:
    def __init__(self, initial_memory: float = 0) -> None:
        """
        Initialize the Calculator with an initial memory value.

        Parameters:
        - initial_memory (float): The initial memory value. Default is 0.
        """
        self.initial_memory: float = initial_memory
        self.memory: float = initial_memory

    def add(self, num: float) -> float:
        """
        Add a number to the memory.

        Parameters:
        - num (float): The number to be added.
        For example:
            >>> calc_instance = CalculatorClass(36)
            >>> calc_instance.add(5)
            41
        """
        self.memory += num
        self.memory = self.memory

        return self.memory

    def subtract(self, num: float) -> float:
        """
        Subtract a number from the memory.

        Parameters:
        - num (float): The number to be subtracted.
        For example:
          >>> calc_instance = CalculatorClass(36)
          >>> calc_instance.subtract(5)
          31
        """
        self.memory -= num
        return self.memory

    def multiply(self, num: float) -> float:
        """
        Multiply the memory by a number.

        Parameters:
        - num (float): The number to multiply the memory by.
        Raises:
         - TypeError: If 'num' is not a float.
        For example:
          >>> calc_instance = CalculatorClass(36)
          >>> calc_instance.multiply(2.0)
          72.0
        """
        if not isinstance(num, float):
            raise TypeError("'num' must be a float.")
        else:
            self.memory *= num
        return self.memory

    def divide(self, num: float) -> float:
        """
        Divide the memory by a number.

        Parameters:
        - num (float): The number to divide the memory by.

        Raises:
        - ValueError: If attempting to divide by zero.
        For example:
          >>> calc_instance = CalculatorClass(36)
          >>> calc_instance.divide(2)
          18.0
        """
        if num != 0:
            self.memory /= num
            return self.memory
        else:
            raise ZeroDivisionError("Cannot divide by zero.")

    def root(self, n: int) -> float:
        """
        Calculate the nth root of the memory.

        Parameters:
        - n (int): The root to be calculated.

        Raises:
        - ValueError: If attempting to calculate the root of a negative number.
        For example:
          >>> calc_instance = CalculatorClass(36)
          >>> calc_instance.root(2)
          6.0
        """
        if n > 0:
            self.memory **= (1 / n)
            return self.memory
        else:
            raise ValueError("Cannot calculate the negative root of a real number.")

    def reset_memory(self) -> float:
        """
        Reset the memory to the initial value.
        """
        self.memory = self.initial_memory
        return self.memory


print(doctest.testmod())
