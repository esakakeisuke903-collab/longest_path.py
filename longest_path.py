# 最長片道きっぷの旅

import sys
sys.setrecursionlimit(10000)

def dfs(current, visited, length, path):
    global max_len, best_path
    # 経路を更新
    if length > max_len:
        max_len = length
        best_path = path[:]

    for nxt, dist in graph[current]:
        if nxt not in visited:
            visited.add(nxt)
            path.append(nxt)
            dfs(nxt, visited, length + dist, path)
            path.pop()
            visited.remove(nxt)


# 入力読み込み
edges = []
while True:
    try:
        line = input().strip()
        if not line:
            break
        a, b, d = line.split(',')
        edges.append((int(a), int(b), float(d)))
    except EOFError:
        break

# グラフ構築（無向）
graph = {}
for a, b, d in edges:
    graph.setdefault(a, []).append((b, d))
    graph.setdefault(b, []).append((a, d))

max_len = 0
best_path = []

# 各駅を出発点に探索
for start in graph.keys():
    dfs(start, {start}, 0, [start])

# 出力
for node in best_path:
    print(node)
