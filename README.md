# Data Structures & Algorithms (DSA) Repository

A comprehensive collection of production-quality Data Structures and Algorithms implementations in C++. This repository provides well-documented solutions organized by topic for educational and professional reference.

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
│   ├── even_odd_pos_neg.cpp      # Even/Odd and Positive/Negative classification
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
└── README.md
```

## 📚 Topics Covered

### 1. Arrays – Single Dimension
- **Kadane's Algorithm**: O(n) solution for maximum sum subarray problem
- **Two Sum**: Efficient approach to find two elements summing to target value
- **Subarray Operations**: Common patterns and techniques

### 2. 2D Arrays – Matrix Operations
- Input/output and efficient traversal
- Row-wise and column-wise computations
- Primary and secondary diagonal operations
- Matrix transformations and searches
- Analysis operations (maximum row sum)

### 3. Trees – Binary Tree Algorithms
- Tree construction and node structure
- Traversal methods:
  - Inorder, Preorder, Postorder
  - Level-order (BFS)
- Standard operations:
  - Node and leaf node counting
  - Search operations
  - Aggregate calculations
- Binary tree input handling

### 4. Strings
- (Section prepared for expansion)

### 5. Competitive Programming – Number Theory & Patterns
- Number theory fundamentals (GCD, divisors, primes)
- Mathematical computations
- Pattern generation algorithms
- Number classification problems

## 🚀 Getting Started

### Prerequisites
- C++ compiler (GCC, Clang, or MSVC)
- C++11 or later
- Basic understanding of data structures and algorithms

### Compilation

```bash
# Standard compilation
g++ -o output_name source_file.cpp

# With modern C++ features
g++ -std=c++17 -o output_name source_file.cpp

# With optimization and warnings
g++ -O2 -Wall -Wextra -std=c++17 -o output_name source_file.cpp
```

### Execution

**Linux/macOS:**
```bash
./output_name
```

**Windows:**
```bash
output_name.exe
```

### Example

```bash
g++ -o kadanes Arrays/Kadanes_algo.cpp
./kadanes
```

## 📖 Complexity Analysis

| Algorithm | Category | Time | Space | Notes |
|-----------|----------|------|-------|-------|
| Kadane's Algorithm | Arrays | O(n) | O(1) | Single pass linear scan |
| Two Sum | Arrays | O(n) | O(n) | Hash map approach |
| Linear Search 2D | 2D Arrays | O(n·m) | O(1) | Brute force search |
| Diagonal Sum | 2D Arrays | O(n²) | O(1) | Matrix iteration |
| Tree Traversals | Trees | O(n) | O(h) | h = tree height |
| Level-Order Traversal | Trees | O(n) | O(w) | w = maximum level width |
| Node Counting | Trees | O(n) | O(h) | Recursive traversal |

## 💡 Key Algorithms

### Array Techniques
- Two-pointer approach
- Sliding window method
- Prefix/suffix optimization

### Matrix Operations
- Row and column iteration
- Diagonal processing
- Space-efficient traversals

### Tree Algorithms
- Recursive depth-first search
- Iterative breadth-first search
- In-place tree modifications

### Number Theory
- Prime factorization
- GCD and LCM computation
- Divisibility analysis

## 📋 Usage Guide

| Use Case | Approach |
|----------|----------|
| Learning algorithms | Study implementation and understand logic |
| Practice problems | Modify test cases and experiment with variations |
| Technical interviews | Reference complexity analysis and core algorithms |
| Project reference | Adapt implementations for specific requirements |

## 🔨 Compilation Flags

| Flag | Purpose | Example |
|------|---------|---------|
| `-std=c++17` | Enable C++17 standard | `g++ -std=c++17 ...` |
| `-O2` | Optimization level 2 | `g++ -O2 ...` |
| `-Wall -Wextra` | Compiler warnings | `g++ -Wall -Wextra ...` |
| `-g` | Debug symbols | `g++ -g ...` |

## 📝 Code Standards

- **Naming Convention**: `snake_case` for variables and functions, `CamelCase` for classes
- **File Naming**: Descriptive names clearly indicating algorithm or problem type
- **Documentation**: Inline comments for complex logic and algorithm explanation
- **Code Style**: Consistent indentation and formatting

## 🛣️ Development Roadmap

- [ ] String matching algorithms (KMP, Z-algorithm)
- [ ] Sorting algorithms (Merge Sort, Quick Sort, Heap Sort)
- [ ] Dynamic Programming solutions
- [ ] Graph algorithms (DFS, BFS, Dijkstra)
- [ ] Stack and Queue data structures
- [ ] Linked List implementations
- [ ] Advanced competitive programming problems

## 📄 License

Educational use. See LICENSE file for details.

---

**Last Updated**: 2026-05-04 12:45:18  
**Language**: C++ (C++11 and later)  
**Algorithm Count**: 30+