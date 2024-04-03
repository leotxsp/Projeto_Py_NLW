class issoai:
    def __enter__(self):
        print("olha eu aqui")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print ("estou saindo")
        

with issoai() as ola:
    print ("estou no meio")