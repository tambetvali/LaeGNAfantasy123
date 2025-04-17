# Four basic operations of math are mapped to get Laegna significance of operations:

For example, in "1 + 2 * 3", plus is executed first as it's in first position, then multiplication. The class here would remove any unfavourable effects from this.

Using "1 + (2 * 3)", the classical order could be emulated.

## Task description

In addition and multiplication operations, such as 1 + 2 * 3, we add mappers at places of operations, such as + and *.

The calculator would do them in order: the plus first and multiplication as second operation.

The mappers want to keep the initial relations of numbers in two groups of operations:
- In multiplication, in this example, the relation is 2:3 between two members of multiplication, but actual relation is 3:3 as 1+2 happens first. 1 + 2 tracks the number 1.5: 1.5 * 2 * 3 = 9.
- In addition, the relation is 1:2 here, but 2 * 3 would be mapped (especially if there would be more additions/subtractions after): lets consider something before 1 + 2. For example, 3 * 1 + 2. 1 + 2 is 3, but 3 + 2 is 5: 3 * 1 is remembered as 2, because in it's place one would add two.
- For division, use the same value in proportion dx = 1 / mx, where d and m are operations, and x is the given value, where you can see the relation between operations.
- For subtraction, use the same value in proportion mx = 0 - px.

There are some special cases:

-2 + 2 * 4 + 1

-2 + 2 would be like multiplying -2 with 0; so write 0 here.

4 + 1 is from zero to one, and maps to multiplication as Y1: it's the infinity value, which as being multiplied with standard zero, would give 1.

With addition and subtraction, it's difficult to achieve any properties of zeroes, which this would not cover - indeed the zero from 1 divided with 2 infinities would keep the proportions, if when the result is multiplied with 4 infinities, one gets 2. I use a specific point for infinity, rather than the "limit" or approximation of all what is left: at certain number, one reaches infinity, but the result is not a last number ("a" is probably a good prefix for a fractal, "the" would be like "the last point").