# Singly Linked List Implementation in Python

A clean, fully‑functional, and beginner‑friendly implementation of a **Singly Linked List** in Python. This project demonstrates object‑oriented programming (OOP), dynamic data structures, and common linked‑list operations.

---

## 🚀 Features

This Linked List class includes the following operations:

### **🔹 Node & LinkedList Classes**

* `Node` class to represent each list element.
* `LinkedList` class to manage nodes and operations.

### **🔹 Insertion Operations**

* `insert_head(value)` – Insert at the beginning.
* `append(value)` – Insert at the end.
* `insert(after, value)` – Insert after a specific value.

### **🔹 Deletion Operations**

* `delete_head()` – Remove the first node.
* `pop()` – Remove the last node.
* `remove(value)` – Remove a node by value.

### **🔹 Utility Methods**

* `__len__()` – Get the size of the list.
* `__str__()` – String representation (e.g., `10 -> 20 -> 30`).
* `__getitem__(index)` – Indexing support like a Python list.
* `search(item)` – Search and return the index of a value.
* `clear()` – Remove all nodes.
* `replace_max(val)` – Replace the maximum value node.
* `reverse()` – Reverse the entire linked list.

---

## 📌 Example Usage

```python
# Creating the Linked List
Mylist = LinkedList()

Mylist.append(10)
Mylist.append(20)
Mylist.append(30)
Mylist.insert(20, 25)
Mylist.remove(10)
Mylist.reverse()
print(Mylist)
print(Mylist.search(20))
Mylist.replace_max(100)
print(Mylist)
Mylist.clear()
print(Mylist)
```

---

## 🧠 Concepts Covered

This project is especially useful for:

* Understanding how dynamic data structures work internally.
* Implementing Linked Lists without relying on Python's built‑in structures.
* Practicing OOP concepts such as constructors, methods, and encapsulation.
* Strengthening knowledge of pointers/references.

---

## 📂 Project Structure

```
linked_list/
├── linked_list.py   # Main implementation
├── README.md        # Documentation
└── examples.py      # Example usage (optional)
```

---

## 🔧 Requirements

* Python 3.x
  No external libraries are required.

---

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for:

* Performance improvements
* Additional linked list operations
* Doubly Linked List or Circular Linked List versions

---

## ⭐ Support

If you found this project helpful, consider giving it a **star** ⭐ on GitHub!
It helps others discover the project and motivates further development.

---

## 📬 Contact

For suggestions or contributions, feel free to open an issue or reach out.

---

### Happy Coding! 💻🎉
