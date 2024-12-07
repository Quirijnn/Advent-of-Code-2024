from bisect import bisect
from typing import List
from itertools import chain

class Por:
    #Por = page ordering rule
    def __init__(self, before, after):
        self.before: int = before
        self.after: int = after

    @classmethod
    def from_string(cls, string):
        before, after = string.split("|")
        return cls(int(before), int(after))

with open("Input/05-12-2024/input5.txt") as f:
    pors, updates = f.read().split("\n\n", 1)

pors, updates = pors.split("\n"), updates.split("\n")
updates = [list(eval(update)) for update in updates]
pors = [Por.from_string(por) for por in pors]

def update_is_valid(update: list, pors: List[Por]):
    for i, page in enumerate(update[:-1]):
        for por in pors:
            if por.before != page:
                continue
            if por.after in update[:i]:
                return False
    return True

def get_last_page(update: list, successor_graph):
    for page in update:
        if not any(page_ in successor_graph[page] for page_ in update if page_ != page):
            last_page = page
    if last_page is None:
        raise ValueError("No page can be last")
    return last_page

def get_successor_graph(pors: List[Por]):
    successor_graph: dict[int: set(int)] = {}
    for page in set(chain.from_iterable([[por.before, por.after] for por in pors])):
        for por in pors:
            if por.before != page:
                continue
            if por.before in successor_graph:
                successor_graph[por.before].add(por.after)
            else:
                successor_graph[por.before] = {por.after}
    return successor_graph

result_valid = 0
result_invalid = 0
successor_graph = get_successor_graph(pors)
for i, update in enumerate(updates):
    if update_is_valid(update, pors):
        result_valid += update[len(update)//2]
    else:
        last_page = None
        ordered_update = []
        for _ in range(len(update)):
            if last_page in update:
                update.remove(last_page)
            last_page = get_last_page(update, successor_graph)
            ordered_update.insert(0, last_page)
        result_invalid += ordered_update[len(ordered_update)//2]
print(result_valid)
print(result_invalid)