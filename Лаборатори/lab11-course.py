# Асуулт

# Та курсын жагсаалттай бөгөөд зарим курс нь бусад курсуудаас хамааралтай байдаг. 
# Бидэнд бүх курсийг амжилттай суралцах боломжтой эсэхийг шалгах хэрэгтэй бөгөөд 
# хэрэв боломжоор хангаж чадвал, курс бүрийг амжилттай суралцах дарааллыг олно уу.
# Бидэнд хоёр зүйл өгөгднө:
#     numCourses: Курсийн тоо
#     prerequisites: Өмнөх шаардлага курсуудын жагсаалт


# graph нь тухайн курсийг шаарддаг бусад курсуудыг хадгалдаг.
# ndegree массив нь тухайн курсийг суралцахаас өмнө хэдэн курс суралцах шаардлагатайг илэрхийлнэ.

# Курс бүрийн хамаарлыг шалгах:
#     Индигри нь 0-тай курсүүдийг эхлээд судалж, эдгээр курсүүдийг суралцах боломжтой гэж үзнэ.
#     Бусад курсийн индигри 1-ээр буурч, индигри 0 болсноор тэднийг дараагийн курс болгон судална.
# Циклийн шалгалт:
#     Хэрэв бүх курсийг зөв дарааллаар суралцаж чадвал тухайн дарааллыг буцаана.
#     Хэрэв цикл илэрвэл, энэ нь курс бүрийг суралцах боломжгүй болохыг илтгэнэ.

from collections import deque, defaultdict

def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses
    
    # Графыг үүсгэж, массивыг шинэчилнэ
    for dest, src in prerequisites:
        graph[src].append(dest)
        indegree[dest] += 1
    
    # массив 0-тай курсүүдийг дараалалд оруулж эхлэх
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    
    # Топологийн эргэлт хийх жагсаалт
    topological_order = []
    
    while queue:
        course = queue.popleft()
        topological_order.append(course)
        
        # Хамааралтай курсүүдийн массивийг бууруулах
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # Хэрэв бүх курсийг амжилттай суралцах боломжтой бол, дарааллыг буцаана
    if len(topological_order) == numCourses:
        return topological_order
    else:
        # Хэрэв цикл байгаа бол хоосон жагсаалт буцаана
        return []

numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(findOrder(numCourses, prerequisites))
