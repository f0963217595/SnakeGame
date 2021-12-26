class Snake:

    def __init__(self):
        self.head = [400,300]
        self.body = [[400,300],[390,300],[380,300]]
        self.dir = "右"

    def move(self):
        if self.dir == "右":
            self.head[0] = self.head[0] + 10
        elif self.dir == "左":
            self.head[0] = self.head[0] - 10
        elif self.dir == "上":
            self.head[1] = self.head[1] - 10
        else:
            self.head[1] = self.head[1] + 10

        #將頭的資料放到身體的第一個索引值
        self.body.insert(0, list(self.head))
        self.body.pop() #將最後一個身體移除
