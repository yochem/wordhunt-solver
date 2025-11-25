import time

Node = dict[str, "Node"]


def load_words(dictionary: str) -> tuple[set[str], Node]:
    allowed = {c for row in grid for c in row}
    words = set()
    # 'apple' -> {'a': {'p': {'p': {'l': {'e': {}}}}}}
    paths: Node = {}
    with open(dictionary, "r") as f:
        lines = f.read().splitlines()

    for word in lines:
        word = word.lower()
        if all(ch in allowed for ch in word):
            words.add(word)
            d = paths
            for char in word:
                d = d.setdefault(char, {})

    return words, paths


def possible_word(path: str) -> bool:
    d = charpaths
    for char in path:
        try:
            d = d[char]
        except KeyError:
            return False

    return True


def paths(grid: list[list[str]]) -> set[str]:
    S = len(grid)
    assert S == len(grid[0])

    results: set[str] = set()
    visited = [[False] * S for _ in range(S)]
    directions = tuple((dy, dx) for dx in (-1, 0, 1) for dy in (-1, 0, 1))

    def walk(y: int, x: int, path: str) -> None:
        visited[y][x] = True
        path += grid[y][x]

        if not possible_word(path):
            visited[y][x] = False
            return

        if path in words:
            results.add(path)

        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < S and 0 <= nx < S and not visited[ny][nx]:
                walk(ny, nx, path)

        visited[y][x] = False

    # start walking from all positions in the grid
    for r in range(S):
        for c in range(S):
            walk(r, c, "")

    return results


def show_rank(results: set[str], minlen: int = 3) -> None:
    per_length: dict[int, list[str]] = {}

    for word in sorted(results):
        per_length[len(word)] = per_length.get(len(word), []) + [word]

    for length, words in sorted(per_length.items(), reverse=True):
        if length <= minlen:
            break
        print(f"Words with {length} characters:")
        print(*words, sep="\n", end="\n\n")


def nbest(results: set[str], n: int = 20) -> list[str]:
    return sorted(results, key=lambda t: len(t), reverse=True)[:n]


if __name__ == "__main__":
    # print('Grid (4x4):')
    # grid = [list(input()), list(input()), list(input()), list(input())]

    grid = [
        ["a", "c", "t", "o"],
        ["s", "n", "t", "e"],
        ["r", "m", "h", "m"],
        ["i", "a", "i", "n"],
    ]
    s = time.time()
    words, charpaths = load_words("/usr/share/dict/words")
    print("load_words", time.time() - s)

    s = time.time()
    res = paths(grid)
    print(f"found {len(res)} words in {(time.time() - s):.4f} seconds")
    # show_rank(res)
    # print(nbest(paths(grid), 10))
