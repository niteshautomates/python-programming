class Lists_Example:
    def print_list_items(self,list):        
        for item in list:
            print(f"{item}")
   

servers = ["payment-service","user-auth-service","gateway-service"]

ec2_instances = ["i-123", "i-456", "i-789"]
# 2. List of Kubernetes pods
pods = ["nginx-pod", "db-pod", "api-pod"]

obj = Lists_Example()
print("List of Servers: \n")
obj.print_list_items(servers)  
print("List of EC2 Instances\n")     
obj.print_list_items(ec2_instances)

print("List of Pods\n")     
obj.print_list_items(pods)


print(ec2_instances.index("i-456"))

my_list = [1, 3, 2, 4, 5]
print(list(reversed(my_list)))
my_list = [1, 3, 2, 4, 5]
print(my_list.sort())