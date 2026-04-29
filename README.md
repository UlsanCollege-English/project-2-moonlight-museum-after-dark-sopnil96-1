# Project 2: Moonlight Museum After Dark

## Team information
- Team name: Moonlight Coders
- Members: Istiaksopnil
- Repository name: project-2-moonlight-museum-after-dark

---

## Project summary
Our project builds a system for organizing museum artifacts after dark using multiple data structures. The system uses a BST to store and search artifacts by ID, a queue to manage restoration requests in order, a stack to undo archive actions, and a singly linked list to manage exhibit routes. Utility functions provide reporting features such as category counts, room lists, age sorting, and name search.

---

## Feature checklist

### Core structures
- [x] `Artifact` class/record
- [x] `ArtifactBST`
- [x] `RestorationQueue`
- [x] `ArchiveUndoStack`
- [x] `ExhibitRoute` singly linked list

### BST features
- [x] insert artifact
- [x] search by ID
- [x] preorder traversal
- [x] inorder traversal
- [x] postorder traversal
- [x] duplicate IDs ignored

### Queue features
- [x] add request
- [x] process next request
- [x] peek next request
- [x] empty check
- [x] size

### Stack features
- [x] push action
- [x] undo last action
- [x] peek last action
- [x] empty check
- [x] size

### Linked list features
- [x] add stop to end
- [x] remove first matching stop
- [x] list stops in order
- [x] count stops

### Utility/report features
- [x] category counts
- [x] unique rooms
- [x] sort by age
- [x] linear search by name

### Integration
- [x] `demo_museum_night()`
- [x] at least 8 artifacts in demo
- [x] demo shows system parts working together

---

## Design note
A BST was chosen for artifact storage because artifact IDs are unique integers, making them ideal BST keys. This allows efficient search, insert, and sorted traversal in O(h) time where h is the tree height. A queue was chosen for restoration requests because museum staff process them in first-come, first-served order — exactly what a queue guarantees. A stack was chosen for undo actions because the most recent action is always the first to be undone, which matches the last-in, first-out behavior of a stack. A singly linked list was chosen for the exhibit route because visitors follow stops in a fixed forward order, and the route changes dynamically as stops are added or removed. The system is organized so that each data structure is its own class with clear methods, and utility functions operate on plain Python lists of Artifact objects for simplicity and flexibility. This separation keeps each component focused and easy to test independently.

---

## Complexity reasoning

- `ArtifactBST.insert`: O(h) where h is the tree height, because the method follows one path from root to the insertion point.
- `ArtifactBST.search_by_id`: O(h) where h is the tree height, because the search follows one path from the root down.
- `ArtifactBST.inorder_ids`: O(n) because every node in the tree is visited exactly once.
- `RestorationQueue.process_next_request`: O(1) because deque removal from the front is constant time.
- `ArchiveUndoStack.undo_last_action`: O(1) because Python list pop from the end is constant time.
- `ExhibitRoute.remove_stop`: O(n) because the list must be traversed to find the matching stop.
- `sort_artifacts_by_age`: O(n log n) because Python's built-in Timsort is used.
- `linear_search_by_name`: O(n) because the list is scanned one item at a time until a match is found.

---

## Edge-case checklist

### BST
- [x] insert into empty tree — root is set to the new node directly.
- [x] search for missing ID — returns None when traversal hits a null node.
- [x] empty traversals — returns empty list when root is None.
- [x] duplicate ID — insert returns False without modifying the tree.

### Queue
- [x] process empty queue — returns None when deque is empty.
- [x] peek empty queue — returns None when deque is empty.

### Stack
- [x] undo empty stack — returns None when list is empty.
- [x] peek empty stack — returns None when list is empty.

### Exhibit route linked list
- [x] empty route — remove_stop returns False, list_stops returns empty list.
- [x] remove missing stop — returns False without modifying the list.
- [x] remove first stop — head is updated to the next node.
- [x] remove middle stop — previous node's next pointer skips the removed node.
- [x] remove last stop — previous node's next is set to None.
- [x] one-stop route — remove sets head to None.

### Reports
- [x] empty artifact list — all utility functions return empty results.
- [x] repeated categories — count_artifacts_by_category increments correctly.
- [x] repeated rooms — unique_rooms returns only distinct room names.
- [x] missing artifact name — linear_search_by_name returns None.
- [x] same-age artifacts — sort_artifacts_by_age preserves stable order.

---

## Demo plan / how to run

```bash
pytest -q
python -c "from src.project import demo_museum_night; demo_museum_night()"
```

---

## Assistance & sources
- AI used? Y
- What it helped with: Structuring the demo function and completing the README.
- Non-course sources used: Python Official Documentation for `collections.deque` and `dataclasses`.
- Links: https://docs.python.org/3/library/collections.html