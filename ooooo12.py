class MyFile:
    def __init__(self, path, mode, encoding = "UTF-8"):
        self.path = path
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        #открываю файл
        self.file = open(self.path, self.mode, encoding = self.encoding )
        return self.file
    
    def __exit__(self,exc_type, exc_val, exc_tb):
        #закрываю файл
        self.file.close()
        



with MyFile("test.txt",'w') as file:  #__enter__  file = self.file
    file.write("Приветики приветики")
#__exit__