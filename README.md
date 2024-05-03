# cosmeticsstore
The provided code implements a simple cosmetics store management system using object-oriented programming (OOP) principles in Python. Let's break down the code and explain its functionality:

1. **Catalog Class (Catalog.py)**:
   - Manages a catalog of items, including makeup and skincare products.
   - Methods include adding items to the catalog, removing items, finding items by ID, printing the catalog, and managing item quantities.

2. **Client Class (Client.py)**:
   - Represents a client with attributes like name, phone number, and balance.
   - Provides methods to get and set client details.

3. **Item Class (Item.py)**:
   - Represents a generic item with attributes such as ID, name, description, price, and quantity.
   - Includes methods to manipulate item quantities and provide string representation of items.

4. **MakeupItem Class (MakeupItem.py)** and **SkinCareItem Class (SkinCareItem.py)**:
   - Subclasses of Item class representing makeup and skincare products respectively.
   - Include additional attributes specific to each type of product (e.g., shade for makeup, area for skincare).

5. **Basket Class (Basket.py)**:
   - Manages a basket for clients to add and remove items for purchase.
   - Includes methods to add items to the basket, remove items, buy items (deducting balance and updating catalog quantities), and display the basket.

6. **CosmeticsStore Class (main.py)**:
   - Main class that orchestrates the functionalities of the cosmetics store system.
   - Manages clients, catalog, and interactions between clients, catalog, and the basket.
   - Provides menu-driven interfaces for clients and administrators to interact with the system.

7. **Readme File**:
   - Not included in the code, but a crucial part of any software project.
   - Contains information about the project, how to set it up, dependencies, usage instructions, etc.

Overall, the code demonstrates a simple implementation of an OOP-based cosmetics store management system, where clients can browse a catalog, add items to their basket, remove items, and make purchases. Administrators can manage the catalog, add clients, and view client details. The system promotes code reusability, encapsulation, and modularity through the use of classes and objects.
