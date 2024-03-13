import heapq #Модуль для роботи з чергою

def dejcstra(graph, start):#функція приймає граф і проймає стартову точку
    #створюємо словник для кожної вершини
    distances ={vertex : float('infinity') for vertex in graph}
    distances[start] = 0 # стартова вершина має значення 0
    #створюємо чергу с пріорітетом для зберігання вершин
    #та відстаней до них
    priority_queue = [(0, start)]
    #перебираємо усі елементи черги
    while priority_queue:
        #знаходимо вершину з найменьшою відстанью
        current_distance, curent_vertex = heapq.heappop(priority_queue)

        #якщо поточний маршрут більше того, що у нас записан
        if current_distance > distances[curent_vertex]:
            continue#продовжуємо перебирати маршрути
        #перебираємо сусудні точки та вагу маршрута
        for neighbor, weight in graph[curent_vertex].items():
            #в дістанцію до точки записали поточну дистанцію +
            # вага маршрута
            distance = current_distance + weight
            #якщо ця дистанція меньше, ніж та, що у нас
            #записана
            if distance < distances[neighbor]:
                #перезаписуємо поточну дистанцію
                distances[neighbor] = distance
                heapq.heappush(priority_queue,(distance,neighbor))
    return distances




graph = {
    'A':{'B':5, 'C':2},
    'B':{'A':5, 'C':1, 'D':3},
    'C':{'A':2, 'B':1,'D':7},
    'D':{'B':3,'C':7}
}

start_vertex = 'A'
short_distance = dejcstra(graph, start_vertex)

print(f"Short distance from {start_vertex}\n to another vertex {short_distance}")