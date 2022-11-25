""" 

This module contains class, attribute, and function/method requires to create a self-service cashier in a supermarket

The user can run this module after defined a variable/object from class using 
<variable = Transaction()>

"""

# Import library which will be use in main.py
import numpy as np

# Create an empty dictionary to store the groceries item
transaction = {}

# Utilised class function to store the attribute and method requires to create a self-service cashier
class Transaction():
    
    def __init__(self):
        
        """ This function is to set the dictionary key and value 
            as the attribute of the class """
        
        for key in transaction:
            setattr(self,key,transaction[key])
    
    def add_item(self, nama_barang, jumlah_barang, harga_barang):
        
        """ 
        This method is utilised to add the groceries item to the empty dictionary
        
        Parameter:
            nama_barang (str): name of the groceries item
            jumlah_barang (int): quantity of the groceries item
            harga_barang (int): each price of the groceries item        
        """
        
        self.nama_barang = nama_barang
        self.jumlah_barang = jumlah_barang
        self.harga_barang = harga_barang
        transaction[self.nama_barang] = [self.jumlah_barang, self.harga_barang]
    
    def update_item_name(self, nama_barang, nama_barang_baru):
        
        """
        This method is utilised to update specific groceries 
        item name stored in the dictionary
        
        Parameter:
            nama_barang (str): name of the groceries item
            nama_barang_baru (str): updated name of the groceries item
        """        
        
        self.nama_barang = nama_barang
        self.nama_barang_baru = nama_barang_baru
        transaction[nama_barang_baru] = transaction[nama_barang]
        del transaction[nama_barang]
        
    def update_item_quantity(self, nama_barang, jumlah_barang_baru):
        
        """
        This method is utilised to update specific groceries 
        item quantity stored in the dictionary
        
        Parameter:
            nama_barang (str): name of the groceries item
            jumlah_barang_baru (int): updated quantity of the groceries item
        """  
        
        self.nama_barang = nama_barang
        self.jumlah_barang_baru = jumlah_barang_baru
        transaction[nama_barang][0] = jumlah_barang_baru
    
    def update_item_price(self, nama_barang, harga_barang_baru):
        
        """
        This method is utilised to update specific groceries 
        item price stored in the dictionary
        
        Parameter:
            nama_barang (str): name of the groceries item
            harga_barang_baru (int): updated price of the groceries item
        """          
        
        self.nama_barang = nama_barang
        self.harga_barang_baru = harga_barang_baru
        transaction[nama_barang][1] = harga_barang_baru
    
    def delete_item(self, nama_barang):
        
        """
        This method is utilised to delete specific groceries 
        item stored in the dictionary
        
        Parameter:
            nama_barang (str): name of the groceries item
        """           
        
        self.nama_barang = nama_barang
        del transaction[nama_barang]
    
    def reset(self):
        
        """
        This method is utilised to delete all groceries 
        item stored in the dictionary
        
        Return:
            Semua item berhasil di delete = All item removed successfully
        """          
        
        transaction.clear()
        print("Semua item berhasil di delete!")
    
    def check_order(self):       

        """
        This method is utilised to check if there is wrong inputation in 
        the groceries item stored in the dictionary based on data type
        
        """      
              
        # Utilised loop to display the key and both values stored in the dictionary
        for key, values in transaction.items():
                                 
            nama_barang = key
            jumlah_barang = values[0]
            harga_barang = values[1]
            
            """
            Utilised branching to check the key and both values stored in the dictionary 
            were inputted correctly
            
            Return:
                Terdapat kesalahan input data = There is a data input error
                Pemesanan sudah benar = Correct order
            
            """
      
            if type(nama_barang) != str:
                print("Terdapat kesalahan input data")
            elif type(jumlah_barang) != int:
                print("Terdapat kesalahan input data")
            elif type(harga_barang) != int:
                print("Terdapat kesalahan input data")
            else:
                print("Pemesanan sudah benar")  

    def display(self):
        
        """
        This method is utilised to display all of the groceries item stored 
        in the dictionary, including showing the total transaction and
        total transaction after discount
        
        """              
        
        # Absolute variable for discount rate
        DISKON_200000 = 5/100
        DISKON_300000 = 8/100
        DISKON_500000 = 10/100
        
        
        # Utilised loop to display all of the groceries item stored in the dictionary
        display_transact = [i for i in transaction.items()] 
        
        # Utilised loop to perform multiplication on multiple values in one key, and using sum to calculate the total transaction
        for key, values in transaction.items():
            transaction[key] = np.prod(values)
            total_belanja = sum(transaction.values())
        
        # Utilised branching to determine the discount rate and therefore calculate the total transaction after discount
        if total_belanja > 200_000 and total_belanja <= 300_000:
            total_belanja_setelah_diskon = total_belanja - (total_belanja * DISKON_200000)
        elif total_belanja > 300_000 and total_belanja <= 500_000:
            total_belanja_setelah_diskon = total_belanja - (total_belanja * DISKON_300000)
        elif total_belanja > 500_000:
            total_belanja_setelah_diskon = total_belanja - (total_belanja * DISKON_500000)
        else:
            total_belanja_setelah_diskon = total_belanja
        
        print(f" Item yang dibeli adalah: {display_transact} \n Total belanja yang harus dibayarkan adalah Rp. {total_belanja} \n Total belanja yang harus dibayarkan setelah diskon adalah Rp. {total_belanja_setelah_diskon}")