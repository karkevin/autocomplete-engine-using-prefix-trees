from __future__ import annotations
from typing import Any, List, Optional, Tuple
from prefix_tree import SimplePrefixTree, CompressedPrefixTree

# autocomplete tests on SimplePrefixTree

if __name__ == '__main__':
    f = SimplePrefixTree('sum')
    print("SIMPLE PREFIX TREE, AVG")
    f.insert('blew', 111.0, ['b', 'l', 'e', 'w'])
    f.insert('ap', 1.0, ['a', 'p'])
    f.insert('cola', 1.0, ['c', 'o', 'l', 'a'])
    f.insert('blew', 111.0, ['b', 'l', 'e', 'w'])
    f.insert('blap', 200.0, ['b', 'l', 'a', 'p'])
    f.insert('adapt', 1.0, ['a', 'd', 'a', 'p', 't'])
    f.insert('adapm', 5.0, ['a', 'd', 'a', 'p', 'm'])
    f.insert('blak', 133.0, ['b', 'l', 'a', 'k'])
    f.insert('blu', 333.0, ['b', 'l', 'u'])
    f.insert('d', 996.0, ['d'])
    f.insert('are', 5.0, ['a', 'r', 'e'])
    f.insert('bleed', 110.0, ['b', 'l', 'e', 'e', 'd'])
    f.insert('cologne', 997.0,
             ['c', 'o', 'l', 'o', 'g', 'n', 'e'])
    f.insert('adam', 991.0, ['a', 'd', 'a', 'm'])
    f.insert('bleep', 1.0, ['b', 'l', 'e', 'e', 'p'])
    print(f)
    print(f.autocomplete(['b', 'l'], None))
    print(f.autocomplete(['b', 'l'], 3))
    print(f.autocomplete(['c'], None))
    print(f.autocomplete(['a', 'd', 'a'], 2))
    f.remove(['a', 'd', 'a', 'm'])
    print("REMOVED ADAM")
    print(f)
    f.remove(['c', 'o', 'l'])
    print("REMOVED COL")
    print(f)
    f.remove(['b', 'l', 'a'])
    print("REMOVED BLA")
    print(f)
    f.remove(['d'])
    print("REMOVED D")
    print(f)

    g = CompressedPrefixTree('sum')
    print("COMPRESSED PREFIX TREE, AVG")
    g.insert('blew', 111.0, ['b', 'l', 'e', 'w'])
    g.insert('ap', 1.0, ['a', 'p'])
    g.insert('cola', 1.0, ['c', 'o', 'l', 'a'])
    g.insert('blew', 111.0, ['b', 'l', 'e', 'w'])
    g.insert('blap', 200.0, ['b', 'l', 'a', 'p'])
    g.insert('adapt', 1.0, ['a', 'd', 'a', 'p', 't'])
    g.insert('adapm', 5.0, ['a', 'd', 'a', 'p', 'm'])
    g.insert('blak', 133.0, ['b', 'l', 'a', 'k'])
    g.insert('blu', 333.0, ['b', 'l', 'u'])
    g.insert('d', 996.0, ['d'])
    g.insert('are', 5.0, ['a', 'r', 'e'])
    g.insert('bleed', 110.0, ['b', 'l', 'e', 'e', 'd'])
    g.insert('cologne', 997.0,
             ['c', 'o', 'l', 'o', 'g', 'n', 'e'])
    g.insert('adam', 991.0, ['a', 'd', 'a', 'm'])
    g.insert('bleep', 1.0, ['b', 'l', 'e', 'e', 'p'])
    print(g)
    print(f.autocomplete(['b', 'l'], None))
    print(f.autocomplete(['b', 'l'], 3))
    print(f.autocomplete(['c'], None))
    print(f.autocomplete(['a', 'd', 'a'], 2))
    g.remove(['a', 'd', 'a', 'm'])
    print("REMOVED ADAM")
    print(g)
    g.remove(['c', 'o', 'l'])
    print("REMOVED COL")
    print(g)
    g.remove(['b', 'l', 'a'])
    print("REMOVED BLA")
    print(g)
    g.remove(['d'])
    print("REMOVED D")
    print(g)
