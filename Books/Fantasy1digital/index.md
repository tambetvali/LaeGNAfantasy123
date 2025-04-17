# Digital mapping of numbers

In my number system, to map initial systems, one needs:

# Conversion 1

- For numbers bigger than zero, to get the new representation substract 1.
- For numbers smaller than zero, add 1.
- Replace initial zero with "U".

This way, the number is frequential, if you use it properly: instead of 10, there is 9, and instead of 100, there is 99: 9, then, is definitely the biggest digit, not something around 1 and 0; also the number length precisely maps multiplication and division logic (which are number length addition and subtraction), where additions and subtraction are more complicated, but also perfectly mapping: adding two numbers of same size together is equal to adding one bit digit to one of them.

# Conversion 2

This result needs this implementation:
- getDigit(base, digit): get one digit
- setDigit(base, digit): set one digit

It would be conscious, is the number bigger or smaller than zero. If it's smaller than zero, the negative digit is such: at this position, give the digit _reversed_, so that in decimal / base-10, 9 becomes 0 and 0 becomes 9. This affects how getDigit works: smaller numbers are smaller than bigger numbers.

The resulting numbers would represent decimal system in my way, and I also use base-4, base-2 etc. systems, which would be represented somehow.

# Conversion 3

Also, the following number would still be converted:
- Sometimes, capital and small letter difference marks whole numbers and fractions, where AAEE.AE is replaced with AAEEae.
  - Whether we use dot or this small-letter notation, we still need: as there is the "U" as zero, we would take the number into second power of digit of the number system, so that there would be only whole digits, then do the -1 / +1 conversion, and then divide with this initial number. Fraction of the most significant digit in fractional part would influence the whole part, for example it's whole number value E depends on each following small letter digit being e.
- Sometimes, capital letters are plus, small letters are minus numbers.

# Conversion 3b

Also implemenet complex numbers, where each digit in given system has real and imaginary part.

Decimal system could be implemented by 1-9 being two-dimensional 1-3, 0 meaning unknown or U digit, or equal to 5 for simplicity (just to get rid of it in the beginning). Two initial numbers would be used.

# Conversion 4

Accept small numbers inside the digits:

AAaaEa would be like AA.aa; E.a - both parts of the number (I use IOAE for base 4 digits!) would be considered separately. Notice that aa here affects the value of AA: A is 1, and from a to e (2) it would be first position of A, where the next big digit E does not care about this misalignment: it is the last whole digit, and where the last A means it's lowest value at precision 2 of "aa", the E would simply add 2 to the result as an E in the last whole number position usually does with what is before it.

You could also use another method with slightly different results: linearize the 0.25 into 1, and 2 into 4, where the 4 values are 0.25, 0.5, 1 and 2: do conversion for such number, and divide by 2 in power of number length. In short: multiply it with 2 in power of number length, as there are 2 values under 1, calculate the value, and divide with 2 in power of number length.
- The task 1 could be followed similarly: the negative number part could be first removed, by adding the range of negative numbers of number of this length, then the value calculate where the number range is in digit list twice; then the same constant subtracted.

If plus and minus digits are represented with small and capital numbers, they can also be mixed, such as:

Aa

A is the positive number, but what follows is negative - from e to a, it's -2. Would there be 0, it would not influence the value of A: being -2, the plus and minus numbers are mixed; -2 would fall off from plus number scope.

What was given about task 1 should be used in this case: a whole number range temporarily in positive range, to calculate the value and convert back.
- Easier and slightly different solution is to have negative digit influence previous positive, and positive digit influence previous negative digits: as the digits are outside digit range, in my math they can influence previous digits: for example, for range OA, E would be outside the range, and instead of being 2 of the current digit, it would be 1 of the last digit. As I have multi-frequential numbers, this is a significant thing to notice

# Conversion 5

Implement unknowns:
- If a digit is unknown, it can be left out of an operation, having only one digit in effect.