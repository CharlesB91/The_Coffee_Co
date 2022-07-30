# The Coffee Co

As a massive coffee love i wanted to create something that i am passion about not. Not something that just gives me my morning kick. I have decided to create this fully featured online coffee shop. This ecommerce application allows users to browser products, make purchases, leave product reviews and post site testimonials. This store ranges from fresh coffee, pod coffee, coffee machines and accessories. 

![Home-Page](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/coffeeclubhomepage.png)

[Deployed Site](https://thecoffeeco.herokuapp.com/)

## User Experience 

I wanted to create an ecommerce web-based application allowing make purchases whilst registered and unregistered. Each product has a corresponding product image with name, description and price. Users can add items to their cart, update and remove items. Once satisfied they can make an online purchase. Users can register for a user account where we can store their address information also. Staff users have access to add products, edit existing products and remove products at their own wish. 

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
- 00000 - is used mostly for the typography.
- F7ECE1 - Is used in the testimonials section as this compliment the background image on the index page. 

### Typography

- For this area i focused one font which is "Bebas Neue", cursive; as feel this creates an assertive tone. This was used from Google Fonts. I then used 'Rubik', sans-serif; for the footer. 

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

- This area is where a user can view the sites testimonials.
- This area is where a registered user can add a testimonial.

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

### Manual Testing

- USER STORY 1: As a site user i can successfully register for a user account - MUST HAVE
[USER STORY 1](https://share.vidyard.com/watch/5a7rXVrjrbUSQK2x6CdE5X?)

- USER STORY 4: As registered and un registered user i can browse the product list - MUST HAVE
[USER STORY 4](https://share.vidyard.com/watch/AJQbcX1xyXCQub35X9kPD9?)

- USER STORY 5: As a registered and un registered user i can search through the full product list using a search bar - MUST HAVE
[USER STORY 5](https://share.vidyard.com/watch/9i7LkkZJhzUGXESihqZSMJ?)

- USER STORY 6: As a registered and unregistered user i can filter through products via price & category - MUST HAVE
[USER STORY 6](https://share.vidyard.com/watch/NUwvnzmkmKdt5KosVdSguq?)

- USER STORY 8: As a registered and unregistered user i can view product details- MUST HAVE
[USER STORY 8](https://share.vidyard.com/watch/XxnmDBV8oLYhN57zXFVywT?)

- USER STORY 9: As a registered and unregistered user i can view each product review - COULD HAVE
[USER STORY 9](https://share.vidyard.com/watch/ZbsjPD4mXgGjThvaZAAYvE?)

- USER STORY 10: As a registered and unregistered i can add multiple items to my cart. I can then view my cart with the grand total price and delivery cost if applicable - MUST HAVE
[USER STORY 10](https://share.vidyard.com/watch/HTMjfZLZ5dYAcwbxBhK1Wn?)

- USER STORY 13: As a registered and unregistered user i can update and remove products from my card - MUST HAVE
[USER STORY 13](https://share.vidyard.com/watch/g4r8JyU4g7zmwDxgA4vQeV?)

- USER STORY 17: As a registered and unregistered user i can make purchases via stripe - MUST HAVE
[USER STORY 17](https://share.vidyard.com/watch/w9iP3GZ9Pkpj3chQHfn39K?)

- USER STORY 7: As a registered and unregistered user i can sort products via price, name & category - COUD HAVE
[USER STORY 7](https://share.vidyard.com/watch/eLDHQoQyTRTZfuAC355RPo?)

- USER STORY 2: As a registered User i can log in successfully using my registered email and password - MUST HAVE
[USER STORY 2](https://share.vidyard.com/watch/WUQYCh13hHV5RnUFQ19PNQ?)

- USER STORY 3: As a registered User i can update my delivery details via the profile area - COULD HAVE
[USER STORY 3](https://share.vidyard.com/watch/nqsRNSSRQ8XQnMD4AbsNUJ?)

- USER STORY 14: As registered user i can leave product reviews - COULD HAVE
[USER STORY 14](https://share.vidyard.com/watch/WyY6V7YVeG4zAQoUD3pWzD?)

- USER STORY 15: As a registered user i can leave site testimonials - COULD HAVE
[USER STORY ](https://share.vidyard.com/watch/8Krtg4SFt2hX1DkAPNbdEc?)

- USER STORY 11: As a admin/staff user i can add products to the site - MUST HAVE
[USER STORY ](https://share.vidyard.com/watch/EYTe6BFAVgZzuataTTCWxp?)

- USER STORY 15: As a admin/staff user i can edit & remove products - MUST HAVE
[USER STORY 15](https://share.vidyard.com/watch/Sa9Sstmk5jyyB9khV3AHPn?)

###  Accessibility Testing

![Home-Page](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/lighthouse-homepage.png)

![Product-List](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/product-list.png)

![Product-Detail](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/product-detail.png)

![Cart](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/cart-lh.png)

![Checkout](https://github.com/CharlesB91/The_Coffee_Co/blob/main/readme/checkout-lh.png)

###  Validator Testing

- Due to extreme time constraints on this product i was unable to complete any validator testing. When testing my site there is no errors being logged in the console therefore i favoured accessibility to be a much more important test for users with required needs. I have noticed this is not an mandatory part of the pass criteria however in the merit. If i had more time i would have conducted in-depth testing. 

## Future Features

### Stock Management

This site would be become fully functional with a stock management system to help staff track product inventory

## **Web Marketing**

### **SEO**

The site has been equipped with a sitemap generated [here](https://www.xml-sitemaps.com/) and robots.txt. 

## **Keywords**

The meta tags and descriptions have been updated for SEO purposes.  The main site does not contain very much copy, other than in the product descriptions and name. 

In order to create the list of keywords for the site, I researched both long and short tail keywords.  

I simply used the google search engine to enhance my key words search by inputting common names ie coffee, fresh coffee etc. 

### **Newsletter**

A customer does not have to be registered in order to sign up for the newsletter.  Anyone who registers to receive the newsletter is automatically added to the newsletter subscribers list in Mailchimp.

### **Facebook**

Social media marketing in the form of Facebook or Instagram is a way to become identifiable to the community you are trying to reach.  For this project I had to set up a Facebook page as part of one of the assessment criteria for the project.

Please note that this page may be removed by Facebook at some point because it is not for a real business.  Therefore I have included two screenshots of the page at time of writing.

## **Deployment and making a clone**

### **Deployment to Heroku**

**In your app** 

1. add the list of requirements by writing in the terminal "pip3 freeze --local > requirements.txt"
2. Git add and git commit the changes made

**Log into heroku**

3. Log into [Heroku](https://dashboard.heroku.com/apps) or create a new account and log in

4. top right-hand corner click "New" and choose the option Create new app, if you are a new user, the "Create new app" button will appear in the middle of the screen

5. Write app name - it has to be unique, it cannot be the same as this app
6. Choose Region - I am in Europe
7. Click "Create App"

**The page of your project opens**

8. Go to Resources Tab, Add-ons, search and add Heroku Postgres

9. Choose "settings" from the menu on the top of the page

10. Go to section "Config Vars" and click button "Reveal Config Vars". 

11. Add the below variables to the list

    * Database URL will be added automatically
    * Secret key - is the djnago secret key can be generated [here](https://miniwebtool.com/django-secret-key-generator/). 

**Go back to your code**

12. Procfile needs to be created in your app
```
web: gunicorn PROJ_NAME.wsgi
```

13. In settings in your app add Heroku to ALLOWED_HOSTS

14. Add and commit the changes in your code and push to github

**Final step - deployment**

15. Next go to "Deploy" in the menu bar on the top 

16. Go to section "deployment method", choose "GitHub"

17. New section will appear "Connect to GitHub" - Search for the repository to connect to

18. type the name of your repository and click "search"

19. once Heroku finds your repository - click "connect"

20. Scroll down to the section "Automatic Deploys"

21. Click "Enable automatic deploys" or choose "Deploy branch" and manually deploy

22. Click "Deploy branch"

Once the program runs:
You should see the message "the app was successfully deployed"

### Forking the GitHub Repository

By forking the GitHub Repository, you will be able to make a copy of the original repository on your own GitHub account allowing you to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository] (https://github.com/CharlesB91/The_Coffee_Co)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository] (https://github.com/CharlesB91/The_Coffee_Co)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open command line interface on your computer
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/CharlesB91/The_Coffee_Co
```

7. Press Enter. Your local clone will be created.

### Setting up your local environment

1. Create Virtual environment on your computer or use gitpod built in virtual environment feature.

2. Create env.py file. It needs to contain those 5 variables.

* Database URL can be obtained from [heroku](https://dashboard.heroku.com/), add PostgreSQL as an add on when creating an app. 
* Secret_key - is the django secret key can be generated [here](https://miniwebtool.com/django-secret-key-generator/). 

```
DEVELOPMENT
SECRET_KEY

STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY 
STRIPE_WH_SECRET

```
PostgreSQL and AWS keys are needed only on Heroku, not in local IDE

3. Run command 
```
pip3 install -r requirements.txt
```
### Getting Stripe keys
Go to developers tab. On side menu you will find API keys. Copy STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY.

Go to Webhooks. Click Add Endpoint button in top right hand corner.
Add endpoint URL (your local or deployed URL)
Add all events 
Than click add endpoint
You should be redirected to this webhook's page. Reveal webhook sign in secret and copy to Settings and to heroku as STRIPE_WH_SECRET variable

### Getting email variables from gmail


- Log into gmail account
- Go to Settings and than See all settings
- Top menu go to Accounts and import
- Find on the list Other google account settings
- Left side menu - Security
- Turn on two step verification: add phone number and follow instructions
- Go back to security
App passwords - Select Mail, Select Device - Other, Django, Copy app password.

In Heroku 
EMAIL_HOST_PASS is the password copied from above.
EMAIL_HOST_USER is the gmail email address

### Setting AWS bucket

1. Go to [Amzon Web Services](https://aws.amazon.com/) page and login or register

2. You should be redirected to AWS Management Console, if not click onto AWS logo in top left corner or click Services icon and choose Console Home

3. Below the header AWS Services click into All Services and find **S3** under Storage

4. Create New Bucket using **Create Bucket** button in top right hand corner

- **Configuration:** type in your chosen name for the bucket (preferably matching your heroku app name) and AWS Region closest to you

- **Object ownership:** ACLs enabled, Bucket owner preferred

- **Block Public Access settings:** Uncheck to allow public access, Acknowledge that the current settings will result that the objects within the bucket will become public

- Click **Create Bucket**

5. You are redirected to Amazon S3 with list of your buckets. Click into the name of the bucket you just created

6. Find the tab **Properties** on the top of the page:
**Static website hosting** at the bottom of the properties page: clik to edit, click enable, fill in index document: index.html and error.html for error

7. On the **Permissions** tab:
- Cross-origin resource sharing (**CORS**) Paste in the below code as configuration and save

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- **Bucket Policy** within permissions tab: Edit bucket policy
Click AWS Policy Generator (top right corner)

Select type of policy: S3 Bucket policy
Principal: * (allows all)
Actions: Get object
Amazon Resource Name (ARN): paste from the Edit bucket policy page in permissions
Click Add statement Than Click Generate Policy and Copy the policy into bucket policy editor. 
In the policy code find "Resource" key and add "/*" after the name of the bucket to enable all
Save changes

- **Access control list (ACL)** within permissions tab: click Edit

find Everyone (public access) and check List box and save

8. Identity and Access Management (IAM)
Go back to the AWS Management Console and find IAM in AWS Services

- side menu - User Groups and click **Create Group**
name group "manage-your-app-name" and click Create group

- side menu - Policies and click **Create Policy**
Click import managed policy - find AmazonS3FullAccess
Copy ARN again and paste into "Resource" add list containing two elements "[ "arn::..", ""arn::../*]" First element is for bucket itself, second element is for all files and foldrs in the bucket

Click bottom right Add Tags, than Click bottom right Next: Review
Add name of the policy and description

Click bottom right Create policy

9. Attach policy to the group we created:
- go to User Groups on side menu
- select your group from the list
- go to permissions tab and add permissions drop down and choose **Attach policies**
- find the policy created above and click button in bottom right Add permissions

10. Create User to go in the group
- **Users** in the side menu and click add users

User name: your-app-staticfiles-user
Check option: Access key - Programmatic access
Click button at the bottom right for Next
- Add user group and add user to the group you created earlier
Click Next Tags and Next: review and Create user
- Download .csv file


11. Connect django to AWS S3 bucket
- install boto3
- install django-storages
- freeze to requirements.txt
- add storages to installed apps in settings.py

```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```

12. Go to heroku to set up environmental variables

open CSV file downloaded earlier and copy each variable into heroku Settings

AWS_STORAGE_BUCKET_NAME
AWS_ACCESS_KEY_ID from csv
AWS_SECRET_ACCESS_KEY from csv
USE_AWS = True
remove DISABLE_COLLECTSTATIC variable from heroku

13. Create file in root directory custom_storages.py

```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

14. Go to settings.py, add the AWS settings

```
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

```

15. To load the media files to S3 bucket

- Go to your S3 bucket page on AWS. Create new folder "media"
- go to the media folder and click Upload

## Bugs

- The only unresolved bug that is outstanding is my order email confirmation. I had spent days trying to figure this out. Every time i submitted a payment stripe would indicate the charge had been succeeded however payment indent was showing as 500 error. After hour of debugging i figured out that the issue was something from the send mail. I tried to many different ways to get this to work with various print statements however nothing would work. In the end i favoured the webhook to be more important that an email confirmation. I spoke to tutor support who indicated its like finding a needle in a haystack and due to time constraints i had to move on.

## Credits

- Boutique Ado walk through provided me with some amazing logic code on how i could get my cart, checkout and profile fully functional. 
- [Unsplash](https://unsplash.com/) for the cool coffee background image in the home page. 
- [www.shopcoffee.co.uk](https://www.shopcoffee.co.uk/shop/buy-coffee-beans-online/) for the product images, names & description
- [asos](https://www.asos.com/) for the layout required to make my cart as simple as possible. 

### **Conclusion**

My coding journey over the last 12 months has been amazing. From starting the simplest html css to creating full stack web application with online payments system. I remember fighting with css when i fist started out now my problems is with webhooks using stripe apis. I feel i have learned so much and due to this course i landed my first job in tech.

As mentioned in this read me due to starting my new job, family i ran into some time constraints on this project. If had more time i would have completed more in-depth validator testing. There is no errors in the console so i am hoping this will be sufficient.. 

I have really enjoyed learning with code institute as the support has been top class. 
