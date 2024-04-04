import json
from collections import deque


def count_connected_components(graph):
    # Khởi tạo một danh sách các đỉnh đã được duyệt qua
    visited = []

    # Khởi tạo số lượng thành phần liên thông ban đầu là 0
    count = 0

    # Duyệt qua tất cả các đỉnh của đồ thị G
    for vertex in graph:
        # Nếu đỉnh chưa được duyệt qua
        if vertex not in visited:
            # Tăng số lượng thành phần liên thông lên 1
            count += 1

            # Duyệt qua tất cả các đỉnh kề của đỉnh hiện tại
            stack = [vertex]
            while stack:
                curr_vertex = stack.pop()
                if curr_vertex not in visited:
                    visited.append(curr_vertex)
                    stack += graph[curr_vertex]

    return count


# # Đọc tập dữ liệu sgb-words vào một danh sách các từ
# with open('sgb-words.txt', 'r') as f:
#     word_list = [word.strip() for word in f.readlines()]
#
# # Tạo một từ điển để lưu trữ đồ thị G
# graph = {}
#
# # Tạo các đỉnh của đồ thị G
# for word in word_list:
#     graph[word] = []
#
# # Tạo các cạnh nối giữa các đỉnh của đồ thị G
# for i in range(len(word_list)):
#     for j in range(i + 1, len(word_list)):
#         if len(word_list[i]) == len(word_list[j]):
#             diff_count = 0
#             for k in range(len(word_list[i])):
#                 if word_list[i][k] != word_list[j][k]:
#                     diff_count += 1
#             if diff_count == 1:
#                 graph[word_list[i]].append(word_list[j])
#                 graph[word_list[j]].append(word_list[i])

# Đọc sẵn rồi lưu vào file G.json để tránh việc phải xây dựng lại mất thời gian

graph = json.load(open('G.json', 'r'))


# Hàm tìm đường đi ngắn nhất từ u đến v trên đồ thị
def shortest_path(graph, u, v):
    # Tạo một dict để lưu trữ đường đi từ u đến các đỉnh khác trên đồ thị
    distances = {u: 0}

    # Tạo một dict để lưu trữ đỉnh cha của mỗi đỉnh trên đường đi từ u đến v
    parents = {u: None}

    # Tạo một hàng đợi để duyệt qua các đỉnh trên đồ thị theo thứ tự BFS
    queue = deque([u])

    # Duyệt qua các đỉnh trên đồ thị theo thứ tự BFS
    while queue:
        curr_vertex = queue.popleft()

        # Nếu đỉnh hiện tại là đỉnh kết thúc, trả về đường đi từ u đến v
        if curr_vertex == v:
            path = [v]
            while parents[v] is not None:
                v = parents[v]
                path.append(v)
            return list(reversed(path))

        # Duyệt qua tất cả các đỉnh kề của đỉnh hiện tại
        for neighbor in graph[curr_vertex]:
            # Nếu đỉnh kề chưa được duyệt qua
            if neighbor not in distances:
                # Cập nhật khoảng cách từ đỉnh bắt đầu đến đỉnh kề
                distances[neighbor] = distances[curr_vertex] + 1

                # Gán đỉnh cha của đỉnh kề là đỉnh hiện tại
                parents[neighbor] = curr_vertex

                # Thêm đỉnh kề vào hàng đợi để duyệt tiếp
                queue.append(neighbor)

    # Nếu không tìm thấy đường đi từ u đến v, trả về None
    return None


c = shortest_path(graph, u='words', v='graph')
print(c)
