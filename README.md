Django Girls with Cloudinary
================================

A simple web application that allows you to uploads photos, maintain a database with references to them, list them with their metadata, and display them using various cloud-based transformations.


Testing [Python Any Where](https://www.pythonanywhere.com/)

Tutorial: [Django Girls](http://tutorial.djangogirls.org/en/installation/index.html)


### Start with virtualenv

We recommend and support the usage of **virtualenv**. All you need to do is create a new virtualenv (if necessary):

    virtualenv venv

And then just activate it:

    source venv/bin/activate




This sample project depends on [Cloudinary's Python library](https://github.com/cloudinary/pycloudinary). 

## Installation

Run the following commands from your shell.

Project cloning and dependent package installation: 

    git clone https://github.com/leonardocintra/django-girls.git
    cd django-girls
    pip install -r requirements.txt

Defining Cloudinary's credentials. The CLOUDINARY_URL value is available in the [dashboard of your Cloudinary account](https://cloudinary.com/console). 
If you don't have a Cloudinary account yet, [click here](https://cloudinary.com/users/register/free) to creare your free acount.
     
    export CLOUDINARY_URL=cloudinary://<API-KEY>:<API-SECRET>@<CLOUD-NAME>