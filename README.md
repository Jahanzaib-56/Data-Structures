# 🐍 Data Structures in Python

## **A Comprehensive Study and Implementation Repository**

Welcome to the **Data Structures in Python** repository! This project serves as a structured collection of code where fundamental computer science **data structures** are implemented from scratch using Python.

The goal is to provide clear, functional, and well-documented implementations to solidify the understanding of how these structures work internally, their performance characteristics, and their practical application.



---

## 🏗️ Repository Structure (Table of Contents)

The repository is organized into numbered folders, with each folder dedicated to a specific data structure. Each folder contains the core implementation file(s) and accompanying unit tests.

| Folder | Data Structure | Description | Key Topics Covered |
| :--- | :--- | :--- | :--- |
| **1. Arrays** | Dynamic Array (List) | Implementation of a **resizable array** from a static array, focusing on the underlying mechanics of **resizing** and **amortized time complexity**. | Indexing, Appending, Insertion, Deletion, Amortized O(1) complexity. |
| **2. Linked Lists** | Singly, Doubly, Circular | Implementations where elements are connected via **pointers** or **references**. Focus on memory management and pointer manipulation. | Head/Tail management, Traversal, Insertion at Head/Tail/Middle, Deletion. |
| **3. Stacks** | LIFO Structure | Implementation using both the **Dynamic Array** and **Linked List** backbones. Focus on the **LIFO** (Last-In, First-Out) principle. | `push`, `pop`, `peek`, Time complexity analysis. |
| **4. Queues** | FIFO Structure | Implementation using both the **Dynamic Array** and **Linked List** backbones. Focus on the **FIFO** (First-In, First-Out) principle. | `enqueue`, `dequeue`, `front`, **Circular Queue** implementation. |
| **5. Hash Tables** | Dictionary/Map | Implementation of the core structure behind Python's `dict`, focusing on **hashing**, **collision resolution** (e.g., separate chaining or open addressing), and load factor. | Hashing function, Collision handling, Load factor, O(1) average time complexity. |
| **6. Trees** | Binary Search Trees (BST) | Implementation of hierarchical structures, focusing on efficient searching and ordering. | Traversal (Inorder, Preorder, Postorder), Insertion, Deletion, Balancing Concepts. |

---

## ⏱️ Time and Space Complexity

A critical part of studying data structures is understanding their performance trade-offs. Each implementation in this repository is designed with complexity in mind.

| Operation | Array (Dynamic) | Linked List (Singly) | Stack (Array/List) | Queue (List) |
| :--- | :--- | :--- | :--- | :--- |
| **Access (Indexing)** | **O(1)** | O(N) | O(1) | O(1) |
| **Search** | O(N) | O(N) | O(N) | O(N) |
| **Insertion (End)** | **Amortized O(1)** | O(1) | **O(1)** | O(1) |
| **Deletion (End/Head)** | O(1) / O(N) | O(N) / O(1) | **O(1)** | O(1) |

> **Note:** The efficiency of an operation is often what determines the suitability of a data structure for a specific task. For example, **O(1)** access is the strength of an Array, while **O(1)** insertion/deletion at the ends is the strength of a Linked List.

---

## 🛠️ Getting Started

To explore and run the code, simply clone the repository and navigate into the desired folder:

1.  **Clone the repository:**
    ```bash
    git clone [YOUR_REPOSITORY_URL]
    ```

2.  **Navigate to a specific structure:**
    ```bash
    cd data-structures-in-python/1. Arrays
    ```

3.  **Run the test file to see the implementation in action (e.g., using Python's built-in testing tools or running the script directly):**
    ```bash
    python dynamic_array.py
    # or
    python test_dynamic_array.py
    ```

Happy coding!
