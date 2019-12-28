import mysql.connector


class zomato:
            def __init__(self):
                self.conn=mysql.connector.connect(host="127.0.0.1",user="root",password="",database="zomato")
                self.mycursor=self.conn.cursor()
                self.program_menu()

            def program_menu(self):
                program_input=input(""" WELCOME TO ZOMATO
                1.Enter 1 to login
                2.Enter 2 to register
                3.Enter anything to exit \n""")

                if program_input=="1":
                    self.login()
                elif program_input=="2":
                    self.register()
                else:
                    print("Thanks for coming here visit again .......")

            def register(self):
                print("Welcome")
                print("Register to use the service")
                name=input("Enter name :")
                email=input("Enter email :")
                phone_num=int(input("Enter phone number :"))
                area=input("Enter your location manually :")


                self.mycursor.execute("""INSERT INTO `users` (`name`, `email`,`phone_num`,`area`)
                 VALUES ('{}', '{}','{}','{}') """.format(name,email,phone_num,area))

                self.conn.commit()
                print("Registered successfully")
                self.program.menu()

            def login(self):
                email=input("Enter the email")
                phone_num=input("Enter the phone number")
                self.mycursor.execute("""SELECT * FROM `users` WHERE `email`
                    LIKE '{}' AND `phone_num` LIKE '{}'""".format(email,phone_num))

                user_list=self.mycursor.fetchall()


                # print(user_list)
                if len(user_list) > 0:
                    print("Welcome")
                    self.current_user_id = user_list[0][0]
                    self.user_menu()
                else:
                    print("Incorrect")
                    self.program.menu()

            def user_menu(self):

                user_input = input("""Hi how would you like to proceed)
                                    1.Select your restaurant from the given all
                                    2.See Order history
                                    3.Anything else to logout""")


                if user_input=="1":
                    self.viewall_restaurant()
                elif user_input=="2":
                    self.view_history()
                else:
                    self.logout()

            def viewall_restaurant(self):
                self.mycursor.execute("""SELECT * FROM `restaurant` """.format(self.current_user_id))
                all_users=self.mycursor.fetchall()

                for i in all_users:
                    print("-->",i[1],"|","Rating=",i[2],"|","Area=",i[3])
                    print("----------------------------------------")
                self.restaurant_id=int(input("Enter the restaurant you want to choose to see for the food menu:"))

                print("\nFood Menu: ")
                self.mycursor.execute("""SELECT * FROM `food` """.format(self.current_user_id))
                food_ordered = self.mycursor.fetchall()
                for i in food_ordered:
                    print(i)
                    print("----------------------------------------")

                self.food_id=int(input("Enter the food items you want to choose :"))
                self.quantity=int(input("Enter how much quantity do you want :"))
                if self.quantity>10:
                    print("Sorry that much quantity not available")
                for i in food_ordered:
                    if(self.food_id==i[0]):
                        print(i[1],"|",i[2])
                        print("----------------------------------------")


                user_input_1= input("""Hi how would you like to proceed
                                    1.Order the food
                                    2.Anything else to logout""")


                if user_input_1=="1":
                    self.order_food()
                else:
                    self.logout()

            def order_food(self):
                print("---------------------BILL---------------------")
                print("FOOD ORDERED")

                self.mycursor.execute("""SELECT * FROM `restaurant` """.format(self.current_user_id))
                all_users=self.mycursor.fetchall()

                for i in all_users:
                    if(self.restaurant_id==i[0]):
                        print(i[1],"|","Rating=",i[2],"|","Area=",i[3],"\n")
                        
                
                self.mycursor.execute("""SELECT * FROM `food` """.format(self.current_user_id))
                food_ordered = self.mycursor.fetchall()
                for i in food_ordered:
                    if(self.food_id==i[0]):
                        price=i[2]
                        print(i[1],"|",i[2],"  Quantity = ",self.quantity," Price = ",price*self.quantity)
                        print("----------------------------------------")
                
                
                
                
                 
            def view_history(self):
                self.mycursor.execute("""SELECT * FROM `proposals` p 
                JOIN `users` u ON u.user_id=p.romeo_id WHERE p.juliet_id={}""".format(self.current_user_id))
                who_proposed=self.mycursor.fetchall()

                for i in who_proposed:
                    print(i[4],"|",i[5],"|",i[7],"|",i[8],"|",i[9])
                    print("----------------------------------------")
                self.user_menu()


            def logout(self):
                self.current_user_id=0
                print("Logout successfully")
                print()

obj1=zomato()
