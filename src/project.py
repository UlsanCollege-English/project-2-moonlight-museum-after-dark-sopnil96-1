from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from typing import Deque


@dataclass(frozen=True)
class Artifact:
    artifact_id: int
    name: str
    category: str
    age: int
    room: str


@dataclass(frozen=True)
class RestorationRequest:
    artifact_id: int
    description: str


class TreeNode:
    def __init__(self, artifact: Artifact, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None) -> None:
        self.artifact = artifact
        self.left = left
        self.right = right


class ArtifactBST:
    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, artifact: Artifact) -> bool:
        if not self.root:
            self.root = TreeNode(artifact)
            return True
        curr = self.root
        while True:
            if artifact.artifact_id == curr.artifact.artifact_id:
                return False
            if artifact.artifact_id < curr.artifact.artifact_id:
                if curr.left is None:
                    curr.left = TreeNode(artifact)
                    return True
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(artifact)
                    return True
                curr = curr.right

    def search_by_id(self, artifact_id: int) -> Artifact | None:
        curr = self.root
        while curr:
            if artifact_id == curr.artifact.artifact_id:
                return curr.artifact
            elif artifact_id < curr.artifact.artifact_id:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def inorder_ids(self) -> list[int]:
        res = []

        def _traverse(node):
            if node:
                _traverse(node.left)
                res.append(node.artifact.artifact_id)
                _traverse(node.right)

        _traverse(self.root)
        return res

    def preorder_ids(self) -> list[int]:
        res = []

        def _traverse(node):
            if node:
                res.append(node.artifact.artifact_id)
                _traverse(node.left)
                _traverse(node.right)

        _traverse(self.root)
        return res

    def postorder_ids(self) -> list[int]:
        res = []

        def _traverse(node):
            if node:
                _traverse(node.left)
                _traverse(node.right)
                res.append(node.artifact.artifact_id)

        _traverse(self.root)
        return res


class RestorationQueue:
    def __init__(self) -> None:
        self._items: Deque[RestorationRequest] = deque()

    def add_request(self, request: RestorationRequest) -> None:
        self._items.append(request)

    def process_next_request(self) -> RestorationRequest | None:
        return self._items.popleft() if self._items else None

    def peek_next_request(self) -> RestorationRequest | None:
        return self._items[0] if self._items else None

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


class ArchiveUndoStack:
    def __init__(self) -> None:
        self._items: list[str] = []

    def push_action(self, action: str) -> None:
        self._items.append(action)

    def undo_last_action(self) -> str | None:
        return self._items.pop() if self._items else None

    def peek_last_action(self) -> str | None:
        return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


class ExhibitNode:
    def __init__(self, stop_name: str, next_node: 'ExhibitNode | None' = None) -> None:
        self.stop_name = stop_name
        self.next = next_node


class ExhibitRoute:
    def __init__(self) -> None:
        self.head: ExhibitNode | None = None

    def add_stop(self, stop_name: str) -> None:
        new_node = ExhibitNode(stop_name)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def remove_stop(self, stop_name: str) -> bool:
        if not self.head:
            return False
        if self.head.stop_name == stop_name:
            self.head = self.head.next
            return True
        curr = self.head
        while curr.next and curr.next.stop_name != stop_name:
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next
            return True
        return False

    def list_stops(self) -> list[str]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.stop_name)
            curr = curr.next
        return res

    def count_stops(self) -> int:
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count


def count_artifacts_by_category(artifacts: list[Artifact]) -> dict[str, int]:
    res = {}
    for a in artifacts:
        res[a.category] = res.get(a.category, 0) + 1
    return res


def unique_rooms(artifacts: list[Artifact]) -> set[str]:
    return {a.room for a in artifacts}


def sort_artifacts_by_age(artifacts: list[Artifact], descending: bool = False) -> list[Artifact]:
    return sorted(artifacts, key=lambda x: x.age, reverse=descending)


def linear_search_by_name(artifacts: list[Artifact], name: str) -> Artifact | None:
    for a in artifacts:
        if a.name == name:
            return a
    return None


def demo_museum_night() -> None:
    print("Moonlight Museum After Dark - Demo: Running Museum Night System...")

    artifacts = [
        Artifact(10, "Ancient Vase", "Ceramic", 500, "Hall A"),
        Artifact(5, "Bronze Sword", "Weapon", 1200, "Hall B"),
        Artifact(15, "Golden Mask", "Jewelry", 3000, "Hall A"),
        Artifact(3, "Clay Tablet", "Document", 4000, "Hall C"),
        Artifact(20, "Marble Bust", "Sculpture", 2000, "Hall B"),
        Artifact(8, "Silk Robe", "Textile", 800, "Hall D"),
        Artifact(1, "Obsidian Blade", "Weapon", 1500, "Hall C"),
        Artifact(12, "Ivory Figurine", "Sculpture", 600, "Hall D"),
    ]

    # BST
    print("\nArtifact BST:")
    bst = ArtifactBST()
    for a in artifacts:
        bst.insert(a)
    print(f"Inorder IDs: {bst.inorder_ids()}")
    print(f"Preorder IDs: {bst.preorder_ids()}")
    print(f"Postorder IDs: {bst.postorder_ids()}")
    print(f"Search ID 8: {bst.search_by_id(8)}")
    print(f"Search missing ID 99: {bst.search_by_id(99)}")
    print(f"Duplicate insert ID 10: {bst.insert(artifacts[0])}")

    # Queue
    print("\nRestoration queue:")
    queue = RestorationQueue()
    queue.add_request(RestorationRequest(10, "Clean vase"))
    queue.add_request(RestorationRequest(5, "Sharpen sword"))
    print(f"Queue size: {queue.size()}")
    print(f"Next restoration request: {queue.peek_next_request()}")
    print(f"Process: {queue.process_next_request()}")
    print(f"Queue size after: {queue.size()}")

    # Stack
    print("\nUndo stack:")
    stack = ArchiveUndoStack()
    stack.push_action("Added Ancient Vase")
    stack.push_action("Added Bronze Sword")
    print(f"Peek action: {stack.peek_last_action()}")
    print(f"Undo action: {stack.undo_last_action()}")
    print(f"Stack size after undo: {stack.size()}")

    # Linked list
    print("\nExhibit route:")
    route = ExhibitRoute()
    route.add_stop("Entrance")
    route.add_stop("Hall A")
    route.add_stop("Hall B")
    route.add_stop("Hall C")
    route.add_stop("Exit")
    print(f"Stops: {route.list_stops()}")
    route.remove_stop("Hall B")
    print(f"After remove: {route.list_stops()}")
    print(f"Stop count: {route.count_stops()}")

    # Utility
    print("\nUtilities:")
    print(f"Category counts: {count_artifacts_by_category(artifacts)}")
    print(f"Unique rooms: {unique_rooms(artifacts)}")
    print(f"Sorted by age: {[a.name for a in sort_artifacts_by_age(artifacts)]}")
    print(f"Search by name: {linear_search_by_name(artifacts, 'Silk Robe')}")
    print(f"Missing name: {linear_search_by_name(artifacts, 'Unknown')}")