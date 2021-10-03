# DS-and-Algo
A playground for practicing Data structure and Algorithm.

Table of contents for Data Structure
=====================================

<!--ts-->
   * [Complexity Analysis](#complexity-analysis)
      * [Time Complexity](#time-complexity)
      * [Space Complexity](#space-complexity)
   * [Memory](#memory)
     * [Bit](#bit)
     * [Byte](#byte)
     * [Fixed-width Integer](#fixed-width-integer)
     * [Memory](#memory)
<!--te-->

# Complexity Analysis
The process of analysing how efficient an algorithm is. Complexity analysis usually involves finding both the **Time Complexity** and the **Space Complexity** of an algorithm.
Complexity analysis is used to effectively determined how "good" an algorithm is and whether it's "better" than another one.

### Time Complexity
A measure of how fast an algorithm runs, time complexity is a central concept in the field of algorithms and coding interviews.
It's expressed using **Big O** notation

### Space Complexity
A measure of how much auxiliary memory an algorithm takes up, space complexity is a central concept in the field of algorithms and coding interviews.
It's expressed using **Big O** notation

# Memory
The bedrock of all data structures, memory is the underlying concept that you absolutely need to know in oredr to understand why data structures work the way they do.

### Bit
Short for **binary digit**, a bit is a fundamental unit of information in Computer Science that represents a state with one of two values, typically **0** and **1**.

# Strings



Any data stored in a computer is, at the most basic level, represented in bits. 

### Byte
A group of 8 **bits**. For example, **01101000** is a byte.

A single byte can represent up to **256** data values **(2^8)**.

Since a **binary number** is a number expressed with only two symbols, like **0** and **1**, a byte can represent all the numbers between 0 and 255, inclusive, in binary format.
Example:

```bash
  1: 00000001
  2: 00000010
```

### Fixed-width Integer
An integer represented by a fixed amount of **bits**. For example, a **32-bit integer** is an integer represented by 32 bits (4 bytes), and a **64-bit integer** is a integer represented by 64 bits (8 bytes).

Regardless of how large an integer is, its fixed-width-integer representation is, by definition, made up of a constant number of bits.

### Memory

Broadly speaking, memory is the foundational layer of computing, where all data is stored.

Important points:
* Data stored in memory is stored in bytes and, by extension, bits.
* Bytes in memory can "point" to other bytes in memory, so as to store references to other data.
* The amount of memory that a machine has is bounded, making it valuable to limit how much an algorithm takes up.
* Accessing a byte or a fixed number of bytes (like 4 bytes or 8 bytes in the case of 32-bit and 64-bit integers) is an elementary operation, which can be loosely treated as a single unit of operational work.


# Strings

```
string = "this is a string"
newString = ""

for char in string:
  newString += char
```

The operation above has a time complexity of **O(n^2)** where n is the length of the **string**. because each addition of a character to **newString** creates an entirely new string and is itself an **O(n)** operation. Therefore, n O(n) operations are performed, leading to an O(n^2) time-complexity operation overall.
