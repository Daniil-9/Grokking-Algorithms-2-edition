graph = {}

graph["вы"] = ["Алиса", "Боб", "Клэр"]
graph["Боб"] = ["Анудж", "Пегги"]
graph["Алиса"] = ["Пегги"]
graph["Клэр"] = ["Том", "Джонни"]
graph["Анудж"] = []
graph["Пегги"] = []
graph["Том"] = []
graph["Джонни"] = []


from collections import deque   # deque используется для создания двусторонней очереди (дека)

def person_is_seller(person):
    if person[0] == "Д":
        return True

def search(name):
    search_queue = deque()  # создание новой очереди
    search_queue += graph[name] # все очереди добавляются в очередь поиска
    searched = set()    #этот массив используется для отслеживания уже проверенных людей
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:  #его проверят если его еще не проверяли
            if person_is_seller(person):
                print(person + " is seller ")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)    #помечаем как проверенный
    return False

search("вы")