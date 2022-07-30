# The Coffee Co

As a massive coffee love i wanted to create something that i am passion about not. Not something that just gives me my morning kick. I have decided to create this fully featured online coffee shop. This ecommerce application allows users to browser products, make purchases, leave product reviews and post site tesimonials. This store ranges from fresh coffee, pod coffee, coffee machines and accessories. 

![Home-Page](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/coffeeclubhomepage.png)

[Deployed Site](https://thecoffeeco.herokuapp.com/)

## User Experience 

I wanted to create an ecommerce web based application allowing make purcases whilst registered and unregistered. Each product has a corresponding product image with name, descriotion and price. Users can add items to their cart, update and remove items. Once satisfied they can make an online purchase. Users can regiser for a user account where we can store their address information also. Staff users have access to add products, edit exisiting products and remove products at their own wish. 

## User Stories

![Kan-ban Board](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/kanban.png)

[Kanban Board](https://github.com/CharlesB91/engage-fitness/projects/1)

With the user stories in mind, I created the below strategy table using MOSCOW principles.

Each story was assigned a classification of Must-Have, Should-Have, Could-Have or Won't Have. Each story was also assigned user story points,

### Unauthorised Users

- USER STORY: As a site user i can successfully register for a user account - MUST HAVE
- USER STORY: As registered and un registered user i can browse the product list - MUST HAVE
- USER STORY: As a registered and un registered user i can search through the full product list using a search bar - MUST HAVE
- USER STORY: As a registered and unregistered user i can filter through products via price & category - MUST HAVE
- USER STORY: As a registered and unregistered user i can view product details- MUST HAVE
- USER STORY: As a registered and unregistered user i can view each product review - COULD HAVE
- USER STORY: As a registered and unregistered i can add multiple items to my cart. I can then view my cart with the grand total price and delivery cost if applicable - MUST HAVE
- USER STORY: As a registered and unregistered user i can update and remove products from my card - MUST HAVE
- USER STORY: As a registered and unregistered user i can make purchases via stripe - MUST HAVE
- USER STORY: As a registered and unregistered user i can sort products via price, name & category - COUD HAVE

### Authorised Users

- USER STORY: As a registered User i can log in successfully using my registered email and password - MUST HAVE
- USER STORY: As a registered User i can update my delivery details via the profile area - COULD HAVE
- USER STORY: As registered user i can leave product reviews - COULD HAVE
- USER STORY: As a registered user i can leave site testimonials - COULD HAVE

### Admin/Staff Users

- USER STORY: As a admin/staff user i can add products to the site - MUST HAVE
- USER STORY: As a admin/staff user i can edit & remove products - MUST HAVE

## Database Model

- Here is a diagram of my database model used in this project.

![Data-Model](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/thecoffeeco.drawio.png)


## Design

### Wireframe

![Wireframes1](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/The%20coffee%20co%20wireframes.jpg)
![Wireframes3](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/The%20coffee%20co%20wireframes2.jpg)
![Wireframes4](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/The%20coffee%20co%20wireframes4.jpg)
![Wireframes5](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/The%20coffee%20co%20wireframes5.jpg)
![Wireframes6](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/The%20coffee%20co%20wireframes8.jpg)

### Colour

![Colour-Pallet1](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/colours1.png)
![Colour-Pallet1](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/colour2.png)

- For this area i focused on only 3 colours for simplicity. 
- FFFFFF - convers the main content area and nav bar
- 00000 - is used mostly for the typograpghy.
- F7ECE1 - Is used in the testimonials section as this compliments the background image on the index page. 

### Typography

- For this area i focused one font which is "Bebas Neue", cursive; as feel this crates an assertive tone. This was used from Google Fonts. I then used 'Rubik', sans-serif; for the footer. 

### Nav Bar

- This area has links to product list, filtering, search box and cart. 

![NarBar](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/nav.png)

### Product List

- This area features a list of each product on sale.
- Users can click on the image to view product detail. 

![Product-List](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/product%20list.png)

### Product Detail

- This area features a detailed description of the product.
- Users can either add to bag, continue shopping, check reviews.

![Product-detail](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/product%20detail.png)

### Reviews

- This area users can view product reviews.
- This is where a registered user can add a product review. 

![Reviews](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/product%20reviews.png)

### Cart

- This is where users can see all the products they have added to their cart.
- This area allows the user to edit, remove items & click checkout. 

![Cart](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/cart.png)

### Checkout

- This area is where the users can fill in their address info and card details to complete purchase.

![Checkout](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/checkout.png)

### Add Product

- This area is restricted to only admin & staff users.
- This is where an admin or staff user can add a product to the site via the sites interface.

![Add-Product](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/add%20product.png)

### Edit/Delete Product

- This area is restricted to only admin & staff users.
- This is where an admin or staff user can edit or delete a product from the sites interface.

### Testimonials

- This area is where a user can view the sites testimontials.
- This area is where a registered user can add a testimontial.

![Testimonials](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/testimonials.png)

## Technologies Used

- HTML5
- CSS3
- JS 
- JQUERY
- Python
- Django
- Postgres SQL
- Materialize CSS
- Stripe

## Testing 

###  Manual Testing

### Unauthorised Users

- USER STORY 1: As a site user i can successfully register for a user account - MUST HAVE
![USER STORY 1](https://share.vidyard.com/watch/5a7rXVrjrbUSQK2x6CdE5X?)


- USER STORY 4: As registered and un registered user i can browse the product list - MUST HAVE


- USER STORY 5: As a registered and un registered user i can search through the full product list using a search bar - MUST HAVE


- USER STORY 6: As a registered and unregistered user i can filter through products via price & category - MUST HAVE


- USER STORY 8: As a registered and unregistered user i can view product details- MUST HAVE


- USER STORY 9: As a registered and unregistered user i can view each product review - COULD HAVE


- USER STORY 10: As a registered and unregistered i can add multiple items to my cart. I can then view my cart with the grand total price and delivery cost if applicable - MUST HAVE


- USER STORY 13: As a registered and unregistered user i can update and remove products from my card - MUST HAVE


- USER STORY 17: As a registered and unregistered user i can make purchases via stripe - MUST HAVE


- USER STORY 7: As a registered and unregistered user i can sort products via price, name & category - COUD HAVE


- USER STORY 2: As a registered User i can log in successfully using my registered email and password - MUST HAVE


- USER STORY 3: As a registered User i can update my delivery details via the profile area - COULD HAVE


- USER STORY 14: As registered user i can leave product reviews - COULD HAVE


- USER STORY 15: As a registered user i can leave site testimonials - COULD HAVE


- USER STORY 11: As a admin/staff user i can add products to the site - MUST HAVE


- USER STORY 15: As a admin/staff user i can edit & remove products - MUST HAVE




