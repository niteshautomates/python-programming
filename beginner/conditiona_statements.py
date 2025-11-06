class ConditionalStatements:
    def if_else_block(self):
        print("*************** IF ELSE BLOCK ***************")
        service_name = input('Enter service name to check status: \n')
        if service_name== "nginx":
            print("\nService is running")
        else:
            print("\nService is not running")     
        


conditional_statements= ConditionalStatements()
conditional_statements.if_else_block()