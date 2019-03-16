# Assignment2
pastebin clone by Gabriele Cateni & Michal Paszcko 

Django Project: 

the web app was broken down into the main django applets and the manage.py and db.sqlite3 files for 
its automated functionalities.
   
  * Within the main project django provides the main app which contains all the files that maintain
    functionality of django. (pastebin_clone)
    
      * setting.py file which contains settings and urls of external resources used by django
      * urls.py file used by django project to map urls of other files to form web app
  
  * We created the blog applet which was meant to control how the users posted and the functionality 
    behind each post. Contained also the basis for main html page. (blog)
    
      * had the migrations directory that contained migrations made for the db tables used
      * had the static directory contain the main css file that would be used by all html pages
      * had the media directory contain user profile images and text files 
      * had the templates directory contain the html files used for the web app, this includes:
      
         * base.html which was the main template for all html pages design 
         * home.html which was the homepage html page for the web app that contained nav bar and list 
           of posts
         * post_confirm_delete.html is used to confirm deletion of post
         * post_detail.html is used to bring up a page for a chosen post for extra info
         * post_form is used to for post creation page
     
      * for the python files there are 5:
         
         * admin.py register models with admin controls
         * apps.py application configurations
         * urls.py maps urls of html pages to main project
         * views.py contains all the functionality used by contents 
         * models.py contains all the classes used for object models
         
  * We created user applet which was meant to control how the user's account/profile and the functionality 
    behind each user:
      
      * had the migrations directory that contained migrations made for the db tables used
      * had the templates directory contain the html files used for the web app, this includes:
      
         * register.html  used for user account creation
         * profile.html used for user profile editing and account deletion
         * login.html used for login for users
         * logout.html used for logout for users
      
      * for the python files there are 6:
         
         * admin.py register models with admin controls
         * apps.py application configurations
         * views.py contains all the functionality used by contents 
         * models.py contains all the classes used for object models
         * forms.py specific forms for creating & updating user profile and accounts
         * signals.py contains all the saving functions for user profiles
  
Additional Resources used in Web App:
  * used bootstrap for styling
  * used django-crispy-forms for automatic styling
  * used Linux tar for backup and crontab -e for scheduling automatic backup of full web app
  * used Let's Encrypt in conjunction with certbot for https certificate 
