class Loops:
    
    def using_for_loop(self):
        print("*************** FOR LOOP ***************")
        servers = ["server-01" , "server-02" , "server-03", "server-04"]
        for server in servers:
            print(f"Deploying on {server}")
            
    def using_while_loop(self):
        print("*************** WHILE LOOP ***************")
        count = 3
        while count > 0:
            print(f"Retrying...{count}")        
            count -= 1
            
            
object = Loops()
object.using_for_loop()   
object.using_while_loop()         