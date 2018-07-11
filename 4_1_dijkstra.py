#python3
#Accepted solution

#Min heap functions
def siftDown(x):
    global heapLen
    mInd=x
    if 2*x+1<heapLen-1:
        l=2*x+1
        if heap[l][1]<heap[mInd][1]or(heap[l][1]==heap[mInd][1] and heap[l][0]<heap[mInd][0]):
            mInd=l
    if 2*x+2<heapLen-1:
        r=2*x+2
        if heap[r][1]<heap[mInd][1]or(heap[r][1]==heap[mInd][1] and heap[r][0]<heap[mInd][0]):
            mInd=r
    if mInd!=x:
        heap[x],heap[mInd]=heap[mInd],heap[x]
        siftDown(mInd)

def siftUp(x):
    par=(x-1)//2
    while x>0 and heap[x][1]<=heap[par][1]:
        if heap[x][1]<heap[par][1]or(heap[x][1]==heap[par][1]and heap[x][0]<heap[par][0]):
            heap[x],heap[par]=heap[par],heap[x]
        x=par
        par=(x-1)//2

def getMin():
    #global heapLen
    result=heap[0]
    if heapLen>2:
        heap[0],heap[heapLen-1]=heap[heapLen-1],heap[0]
        heap.pop()
    siftDown(0)
    return result

def ins(x):
    heap.append(x)
    siftUp(heapLen-1)
#Heap functions end

def heapify():
    #global heapLen
    for i in range(heapLen//2-1,-1,-1):
        siftDown(i)

def changePriority(x):
    global heapLen
    heap.append(x)
    heapLen+=1
    siftUp(heapLen-1)

def printAdjL():
    print('\n'.join(' '.join(str(i[0])+","+str(i[1]) for i in row) for row in adjL))

def printHeap():
    print('\n'.join(' '.join(str(i) for i in row) for row in heap))

g=input()
n=int(g.split()[0])
m=int(g.split()[1])
adjL=[]
for i in range(n+1):
    adjL.append([])
for i in range(m):
    e=input()
    adjL[int(e.split()[0])].append([int(e.split()[1]),int(e.split()[2])])
inp=input()
orig=int(inp.split()[0])
dest=int(inp.split()[1])
dist=[100000001]*(n+1)
prev=[0]*(n+1)
dist[orig]=0
heap=[]
for i in range(1,n+1):
    heap.append([i,dist[i]])
heapLen=n
heapify()
while heapLen>0:
    u=getMin()
    heapLen-=1
    for v in adjL[u[0]]:
        if dist[v[0]]>dist[u[0]]+v[1]:
            dist[v[0]]=dist[u[0]]+v[1]
            prev[v[0]]=u[0]
            changePriority([v[0],dist[v[0]]])
if dist[dest]!=100000001:
    print(dist[dest])
else:
    print(-1)
