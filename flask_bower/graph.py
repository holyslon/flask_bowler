# -*- coding: utf-8 -*-
from Queue import Queue


class Node:

    def __init__(self, data, container=None):
        self.data = data
        self.container = container or []

    def add(self, node):
        self.container.append(node)

    def __str__(self):
        return "%s: %s" % (str(self.data), str(self.container))

    def __repr__(self):
        return "%s: %s" % (str(self.data), str(self.container))

    def __getitem__(self, key):
        return self.container[key]

    def __len__(self):
        return len(self.container)

    def __iter__(self):
        return iter(self.container)


def linerise_graph(nodes):
    cache = Queue()
    for node in nodes:
        cache.put(node)
    while not cache.empty():
        node = cache.get()
        for sub_node in node:
            cache.put(sub_node)
        yield node
