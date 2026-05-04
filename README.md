# Data Structures & Algorithms (DSA) Repository

A comprehensive collection of Data Structures and Algorithms implementations in C++. This repository contains solutions to various DSA problems organized by topic for easy reference and learning.

## 📁 Repository Structure

```
DSA/
├── Arrays/
│   ├── Kadanes_algo.cpp          # Maximum subarray sum (Kadane's Algorithm)
│   ├── subarrays.cpp             # Subarray operations and problems
│   └── two_sum.cpp               # Two sum problem
├── 2D_Arrays/
│   ├── 2d_array_input.cpp        # 2D array input/output operations
│   ├── colsum.cpp                # Column sum calculations
│   ├── Diagonal_sum.cpp          # Diagonal sum (primary & secondary)
│   ├── linear_scearch_2D.cpp     # Linear search in 2D arrays
│   ├── maxisum_row_sum.cpp       # Maximum row sum
│   └── mirror_matrix.cpp         # Mirror matrix operations
├── Tree/
│   ├── count_leaf_nodes.cpp      # Count total leaf nodes
│   ├── count_nodes.cpp           # Count total nodes in tree
│   ├── creating_tree.cpp         # Binary tree creation and traversals
│   ├── Input_binary_tree.cpp     # Taking binary tree input
│   ├── is_node_present.cpp       # Search for node in tree
│   ├── level_order_traversal.cpp # BFS/Level-order traversal
│   └── sum_of_nodes.cpp          # Sum of all node values
├── strings/
│   └── (Placeholder for string algorithms)
├── codeforces/
│   ├── 1-to_n.cpp                # Numbers 1 to N problems
│   ├── digits.cpp                # Digit manipulation
│   ├── divisors.cpp              # Divisor problems
│   ├── even_odd_pos_neg.cpp      # Even/Odd and Positive/Negative
│   ├── even.cpp                  # Even number problems
│   ├── factorial.cpp             # Factorial calculation
│   ├── gdc.cpp                   # Greatest Common Divisor
│   ├── lucky.cpp                 # Lucky number problems
│   ├── max.cpp                   # Maximum element problems
│   ├── multiplication.cpp        # Multiplication operations
│   ├── numbers_histogram.cpp     # Histogram of numbers
│   ├── palindrome.cpp            # Palindrome checking
│   ├── password.cpp              # Password-related problems
│   ├── prime.cpp                 # Prime number checking
│   ├── primes1ton.cpp            # Find all primes 1 to N
│   ├── pyramid.cpp               # Pyramid pattern problems
│   └── shape1.cpp                # Shape pattern problems
└── README.md                     # This file
```

## 📚 Topics Covered

### 1. **Arrays** - Single Dimension
- **Kadane's Algorithm**: Find maximum sum subarray in O(n) time
- **Two Sum**: Find two elements that add up to target
- **Subarray Problems**: Various operations on subarrays

### 2. **2D Arrays** - Matrix Operations
- Array input/output and traversal
- Row-wise and column-wise operations
- Diagonal sum calculations (primary and secondary)
- Matrix transformations (mirror, transpose)
- Linear search in 2D structures
- Matrix analysis (max row sum)

### 3. **Trees** - Binary Trees
- Tree node structure and creation
- Tree traversals:
  - Preorder, Inorder, Postorder
  - Level-order (BFS) traversal
- Tree operations:
  - Count nodes and leaf nodes
  - Find nodes
  - Calculate sum of nodes
- Binary tree construction from input

### 4. **Strings** - (Section ready for expansion)

### 5. **Competitive Programming** - Codeforces Problems
- Number theory problems (GCD, divisors, primes)
- Mathematical operations (factorial, combinations)
- Pattern generation (pyramids, shapes)
- Number properties (palindromes, lucky numbers)
- Array element classification (even/odd, positive/negative)

## 🚀 Quick Start

### Prerequisites
- C++ compiler (g++, clang, or MSVC)
- Basic knowledge of data structures and algorithms

### Compilation and Execution

```bash
# Compile a program
g++ -o output_name source_file.cpp

# Run the program
./output_name

# Example: Compile and run Kadane's algorithm
g++ -o kadanes Arrays/Kadanes_algo.cpp
./kadanes
```

### For Windows (PowerShell/CMD)
```bash
# Compile
g++ -o output_name source_file.cpp

# Run
.\output_name.exe
```

## 📖 Algorithm Complexity Reference

| Algorithm | Topic | Time Complexity | Space Complexity |
|-----------|-------|-----------------|------------------|
| Kadane's | Arrays | O(n) | O(1) |
| Two Sum | Arrays | O(n) | O(n) |
| Linear Search 2D | 2D Arrays | O(n*m) | O(1) |
| Diagonal Sum | 2D Arrays | O(n²) | O(1) |
| Tree Traversals | Trees | O(n) | O(h) |
| Count Nodes | Trees | O(n) | O(h) |
| Preorder/Inorder/Postorder | Trees | O(n) | O(h) |
| Level Order | Trees | O(n) | O(w) |

*h = height, w = width (max nodes at a level)*

## 💡 Key Concepts

### Array Algorithms
- Sliding window and two-pointer techniques
- Maximum subarray problems
- Sorting and searching

### 2D Array Operations
- Matrix traversal patterns
- Row and column operations
- Diagonal operations

### Tree Algorithms
- Recursive tree traversals
- Tree node counting
- Depth-first and breadth-first search

### Number Theory (Competitive Programming)
- Prime factorization
- GCD/LCM calculations
- Divisibility properties

## 🎯 How to Use This Repository

1. **For Learning**: Navigate to relevant topics and study implementations
2. **For Practice**: Compile and run programs with different test cases
3. **For Reference**: Use as a quick lookup for algorithm implementations
4. **For Interview Prep**: Review common algorithms and their complexities

## 🔧 Build Tips

- Use `-std=c++17` flag for modern C++ features: `g++ -std=c++17 -o output file.cpp`
- Add `-Wall -Wextra` flags for better error checking: `g++ -Wall -Wextra -o output file.cpp`
- Optimize with `-O2` flag: `g++ -O2 -o output file.cpp`

## 📝 File Naming Convention

- **snake_case**: Used for most files (e.g., `kadanes_algo.cpp`)
- **CamelCase**: Used for some files (e.g., `Diagonal_sum.cpp`)
- **Descriptive Names**: All files named to clearly indicate their algorithm/problem

## 🤝 Contributing

Feel free to extend this repository with:
- Additional algorithms
- Optimized solutions
- Alternative approaches
- Better explanations
- More complex problems

## 📌 Future Additions

- [ ] Complete strings folder with string algorithms
- [ ] Sorting algorithms (Merge Sort, Quick Sort, Heap Sort, etc.)
- [ ] Dynamic Programming problems
- [ ] Graph algorithms
- [ ] Stack and Queue operations
- [ ] Linked List implementations
- [ ] More competitive programming problems

## 📄 License

This repository is open source and available for educational purposes.

## 🙋 Support

For questions or suggestions:
- Review the code comments and inline explanations
- Test with different inputs
- Compare with standard algorithm textbooks
- Modify and experiment with the code

---

**Last Updated**: May 2026
**Language**: C++
**Total Problems**: 30+
