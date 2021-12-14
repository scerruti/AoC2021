'''Visualize a tree'''

from itertools import (chain, repeat, starmap)
from operator import (add)


# drawTree :: Tree a -> String
def drawTree(tree):
    '''ASCII diagram of a tree.'''
    return '\n'.join(draw(tree))


# draw :: Tree a -> [String]
def draw(node):
    '''List of the lines of an ASCII
       diagram of a tree.'''

    def shift(first, other, xs):
        return list(starmap(
            add,
            zip(
                chain([first], repeat(other, len(xs) - 1)),
                xs
            )
        ))

    def drawSubTrees(xs):
        return (
            (
                    ['│'] + shift(
                '├─ ', '│  ', draw(xs[0])
            ) + drawSubTrees(xs[1:])
            ) if 1 < len(xs) else ['│'] + shift(
                '└─ ', '   ', draw(xs[0])
            )
        ) if xs else []

    return (node.name).splitlines() + (
        drawSubTrees(node.children)
    )


class Node:
    def __init__(self, name=None, cave_system=None):
        if name:
            self.name = name
        else:
            self.name = None

        self.children = []
        self.isSmall = name[0].islower()
        cave_system[name] = self

    def print(self):
        print(self.name, end=' ')
        if len(self.children) > 0:
            for child in self.children:
                child.print()
        else:
            print('.')

    def navigate(self, path):
        if self.isSmall and self.name in path:
            return []

        if path:
            path = ','.join([path, self.name])
        else:
            path = self.name

        if self.name == 'end':
            return [path]

        if len(self.children) == 0:
            return []

        paths = []
        for child in self.children:
            paths.extend(child.navigate(path))
        return paths

    def navigate2(self, path, two_small_visited=False):
        if (self.name == 'start' and self.name in path) or \
                (self.isSmall and path.count(self.name) > 1) or \
                            (self.isSmall and two_small_visited and self.name in path):
            return []

        if path:
            path = ','.join([path, self.name])
        else:
            path = self.name

        if self.isSmall and path.count(self.name) > 1:
            two_small_visited = True

        if self.name == 'end':
            return [path]

        if len(self.children) == 0:
            return []

        paths = []
        for child in self.children:
            paths.extend(child.navigate2(path, two_small_visited))
        return paths


def add_path(cave_system, a, b):
    node_a = cave_system[a] if a in cave_system else Node(a, cave_system)
    node_b = cave_system[b] if b in cave_system else Node(b, cave_system)

    node_b.children.append(node_a)
    node_a.children.append(node_b)


def main(file):
    cave_system = {}
    start = Node('start', cave_system)

    with open(file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        a, b = line.strip().split('-')
        add_path(cave_system, a, b)
        print('adding {}, {}'.format(a, b))

    paths = start.navigate('')
    for path in paths:
        print(path)
    print(len(paths))

    paths = start.navigate2('')
    for path in paths:
        print(path)
    print(len(paths))


if __name__ == '__main__':
    main('input.txt')
