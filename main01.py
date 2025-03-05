

import products as pr



def main():
    products = []

    laptop = pr.Product(
        'Laptop', 
         800,
         '15-inch display, 8GB RAM, 256GB SSD'
        )
    laptop.display()
    print('__dict__',laptop.__dict__)
    print('__module__',laptop.__module__)
    print('__repr__',laptop.__repr__)
    print('__str__',laptop.__str__)
    
    products.append(laptop)
    
    smarthpone = pr.Product(
        'Smarthphone',
        500.00,
        '6-inch display, 128gb ssd'

    )
    smarthpone.display()
    products.append(smarthpone)
    
    
    print(products)






if __name__ == '__main__':
    main()