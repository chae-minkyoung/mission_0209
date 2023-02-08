class Graph() :
    def __init__ (self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

## 전역 변수 선언 부분 ##
G1 = None
stack = []
visitedAry = []		# 방문한 정점
price=[]
## 메인 코드 부분 ##
G1 = Graph(5)
G1.graph[0][2] = 1; G1.graph[0][2] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1; G1.graph[1][3] = 1
G1.graph[2][1] = 1; G1.graph[2][2] = 1
G1.graph[3][1] = 1; G1.graph[3][2] = 1; G1.graph[3][4] = 1
G1.graph[4][3] = 1

stores=[['GS25',30],['CU',60],['Seven11',10],['Ministop',90],['Emart24',40]]

print(end='\t   ')
for i in range(5):
    print('%8s'%stores[i][0],end='')
print()
for row in range(5) :
    print('%8s'%stores[row][0],end='')
    for col in range(5) :
        print('%7d'%G1.graph[row][col], end = ' ')
    print()

current = 0		# 시작 정점 A
stack.append(current)
visitedAry.append(current)
price=current
price=stores[0]

while len(stack) != 0:
    next = None
    for vertex in range(5):
        if G1.graph[current][vertex] == 1 :
            if vertex in visitedAry :  	   # 방문한 적이 있는 정점이면 탈락
                pass
            else : 			   # 방문한 적이 없으면 다음 정점으로 지정
                next = vertex
                break

    if next != None :			  	   # 다음에 방문할 정점이 있는 경우
        current = next
        stack.append(current)
        visitedAry.append(current)
        if stores[current][1]>price[1]:
            price=stores[current]
    else :            	  	  	  	  # 다음에 방문할 정점이 없는 경우
        current = stack.pop()

print(price)


