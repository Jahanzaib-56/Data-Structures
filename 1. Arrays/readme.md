# 📚 Data Structures in Python: 1. Arrays

## **Dynamic Array Implementation (Python List from Scratch)**

Welcome to the **1. Arrays** folder! This directory contains the foundational code for one of the most common and versatile data structures: the **Dynamic Array**.

In Python, the built-in **`list`** object is implemented as a dynamic array. This project is an educational exercise where I implement the core logic of a dynamic array from scratch using a low-level static array (like the `ctypes` module or a standard Python list used as a fixed-size container) to replicate the behavior and operations of the built-in `list` object.

### ❓ What is a Dynamic Array?

A **Dynamic Array** (or *resizable array*) is a sequence data structure that overcomes the size limitations of a traditional **Static Array**.

* **Static arrays** have a fixed size defined at creation; if you need to add more elements than capacity, the operation fails.
* **Dynamic arrays** automatically manage this by **resizing** themselves (usually doubling their capacity) when they become full. This automatic resizing is the "dynamic" part of the structure.



***

## 🚀 `DynamicArray` Class Features

The custom `DynamicArray` class implemented here provides all the essential methods and operations you'd expect from a Python list, demonstrating a deep understanding of how these operations work under the hood.

| Feature | Built-in Python List Method | Custom Implementation Method | Description | Time Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Length** | `len(my_list)` | `__len__` | Returns the number of elements in the array. | **O(1)** |
| **Access** | `my_list[i]` | `__getitem__` | Accesses an element by its index. | **O(1)** |
| **Assignment** | `my_list[i] = x` | `__setitem__` | Modifies an element at a given index. | **O(1)** |
| **Iteration** | `for x in my_list` | `__iter__` | Allows for looping through all elements. | **O(N)** |
| **Append** | `my_list.append(x)` | `append` | Adds an element to the end, triggering **resizing** if capacity is reached. | **Amortized O(1)** |
| **Insert** | `my_list.insert(i, x)` | `insert` | Inserts an element at a specific index, shifting subsequent elements. | **O(N)** |
| **Delete** | `del my_list[i]` | `__delitem__` | Deletes an element at a specific index, shifting subsequent elements. | **O(N)** |
| **Pop** | `my_list.pop()` | `pop` | Removes and returns the last element. | **O(1)** |
| **String Repr.** | `str(my_list)` | `__repr__` | Provides a clean, official string representation. | **O(N)** |

***

## 🛠️ Implementation Details: How Resizing Works

The most crucial operation in a dynamic array is the **resizing** process, which ensures the array never overflows. This is handled by the private `_resize` method.

1.  **Check Capacity:** When an `append` or `insert` operation is called, the array checks if the current size equals the capacity.
2.  **New Array Allocation:** If full, a **new, larger static array** is allocated (e.g., with double the capacity).
3.  **Element Migration:** All elements from the old, smaller array are copied over to the newly allocated array.
4.  **Reference Update:** The internal reference is updated to point to the new, larger array.
5.  **Operation Completion:** The original operation (e.g., the append) is completed on the new array.

This approach ensures that while a single resize operation is **O(N)** (due to copying all N elements), the **average** or **amortized** cost of an `append` operation remains **O(1)** because resizing events are infrequent.

***

## 📂 File Structure

* `dynamic_array.py`: Contains the complete **`DynamicArray`** class implementation.
* `README.md`: You are currently reading this file!
