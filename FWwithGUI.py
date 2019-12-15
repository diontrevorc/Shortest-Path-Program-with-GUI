import tkinter as tk
from tkinter import font
from PIL import ImageTk,Image

HEIGHT=620
WIDTH=750
 
INF = 99999
seq_matrix=[[0, 1, 2, 3, 4, 5, 6, 7, 8],
            [0, 0, 2, 3, 4, 5, 6, 7, 8],
            [0, 1, 0, 3, 4, 5, 6, 7, 8],
            [0, 1, 2, 0, 4, 5, 6, 7, 8],
            [0, 1, 2, 3, 0, 5, 6, 7, 8],
            [0, 1, 2, 3, 4, 0, 6, 7, 8],
            [0, 1, 2, 3, 4, 5, 0, 7, 8],
            [0, 1, 2, 3, 4, 5, 6, 0, 8],
            [0, 1, 2, 3, 4, 5, 6, 7, 0]
	  ]

adjacency_matrix = [[  0, 4, INF, INF, INF, INF, INF, 8, INF],
	            [  4, 0, 8, INF, INF, INF, INF, 11, INF],
	            [ INF, 8, 0, 7, INF, 4, INF, INF, 2],
	            [ INF, INF, 7, 0, 9, 14, INF, INF, INF],
                    [ INF, INF, INF, 9, 0, 10, INF, INF, INF],
                    [ INF, INF, 4, 14, 10, 0, 2, INF, INF],
                    [ INF, INF, INF, INF, INF, 2, 0, 1, 6],
                    [ 8, 11, INF, INF, INF, INF, 1, 0, 7],
                    [ INF, INF, 2, INF, INF, INF, 6, 7, 0]
                  ]

def path(source,destination):
    src = int(source)
    dst = int(destination)
    arr = []
    
    if src>8 or dst>8:
        if src>8 and dst>8:
            final_str='Vertices do not exist.'
        elif src>8:
            final_str='Vertex %s does not exist.' %(src)
        else:
            final_str='Vertex %s does not exist.' %(dst)
    elif src == dst:
        final_str='Destination is same as source.'
        
    else:
        i = src
        j = dst
        m = seq_matrix[i][j]
        if m != j:
            while seq_matrix[i][j] != j:
                v = seq_matrix[i][j]
                arr.insert(0,'  -->  ')
                arr.insert(0,v)
                j = v
            j = dst
            while seq_matrix[m][j] != j:
                arr.append(seq_matrix[m][j])
                arr.append('  -->  ')
                m = seq_matrix[m][j]
                
        arr.insert(0,'  -->  ')
        arr.insert(0, src)
        arr.append(dst)
        
        result=' '
        for element in arr:
            result +=str(element)
        start='From %s to %s: ' %(src, dst)
        end='  (distance %s)' %(adjacency_matrix[i][j])
        final_str=str(start) + str(result) + str(end)
        
    label['text']=final_str
   
def floyd_warshall(vertex, adjacency_matrix):
    for k in range(0, vertex):
        for i in range(0, vertex):
            for j in range(0, vertex):
                if adjacency_matrix[i][k] + adjacency_matrix[k][j]<adjacency_matrix[i][j]:
                    adjacency_matrix[i][j]=adjacency_matrix[i][k] + adjacency_matrix[k][j]
                    seq_matrix[i][j]=k


floyd_warshall(9, adjacency_matrix)


root=tk.Tk()
root.title("GUI")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame=tk.Frame(root, bg='#067cd1', bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.25, anchor='n')

entry_destination = tk.Entry(frame)
entry_destination.place(relx=0.22, rely=0.4, relwidth=0.46, relheight=0.2, anchor='nw')

entry_source=tk.Entry(frame)
entry_source.place(relx=0.22, rely=0.25, relwidth=0.46, relheight=0.2, anchor='sw')

button = tk.Button(frame, text="Find Shortest Route", command=lambda:path(entry_source.get(), entry_destination.get())) 
button.place(relx=0.7, rely=0.075, relheight=0.5, relwidth=0.3)

lower_frame=tk.Frame(root, bg='#067cd1', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg='white', anchor='sw', justify='left', font=('Roboto', 11))
label.place(relwidth=1, relheight=1)

source_label = tk.Label(frame, text="Source", bg='#C5C2C2')
source_label.place(relx=0.01, rely=0.25, relwidth=0.2, relheight=0.2, anchor='sw')

destination_label = tk.Label(frame, text="Destination", bg='#C5C2C2')
destination_label.place(relx=0.01, rely=0.4, relwidth=0.2, relheight=0.2, anchor='nw')

img = Image.open("filename5_edge.png")
img = img.resize((544, 306), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(img)
image=tk.Label(lower_frame, image=photoImg)
image.place(relx=0.5, rely=0, relwidth=0.975, relheight=0.86, anchor='n')

root.mainloop()
