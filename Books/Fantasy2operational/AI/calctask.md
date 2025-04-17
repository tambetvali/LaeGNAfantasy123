Can you create a simple calculator:

- It would execute operations +, -, * and / in Python, given a _string_ of numbers and operations.

- It would consider these operations operations, and parse all the rest as numbers, removing whitespace around them: if number parsing does not work, it would express that it's not a number.

- For "1 + 2 * 3", it would use this order: first plus, then multiplication, in order they are written.

- For "1 + (2 * 3)", classical order would be followed: it would first multiply, then add.

- "+" does not have higher precedence: the order is used instead, where in "1 + 2 * 3" addition occurs before multiplication, and in "3 * 2 + 1", multiplication comes first: it's like if you write each operation on separate line, where one executes them algorithmically rather than mathematically.
