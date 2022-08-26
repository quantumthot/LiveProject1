# Python Live Project

<h2>Introduction</h2>

This is a code summary of a live group project I worked on over a two week sprint, while attending The Tech Academy. I created a web-based UI application that utilizes various Python and Django features. In the "Snow Report" app, there are databases to keep track of data, use of data scraping to collect and aggrigate data, and more! You can save your favorite ski resort, and see the local temperature. This project is built using Python, Django, SQLite, Bootstrap, Jquery, and HTML/CSS. It was really great working on a team, 


<h2>CRUD Functionality</h2>

The main CRUD functionality of this project is to have the ability of saving, updating, or deleting your favorite ski resort. Including saved information of ticket prices and conditions.

<h2>Create</h2>

Here I created a couple of models for the project using Python. Entry is the form to be able to save your resorts uwith Django.

from django.db import models

class Entry(models.Model):<br>
    resort = models.CharField(max_length=50)<br>
    location = models.CharField(max_length=100)<br>
    tickets = models.CharField(max_length=50, default='')<br>
    date = models.CharField(max_length=50)<br>
    conditions = models.TextField(max_length=1000)<br>
    # Model manager<br>
    Entries = models.Manager()<br>

    def __str__(self):<br>
        return self.resort<br>


class WeatherMoment(models.Model):<br>
    temperature = models.IntegerField()<br>
    date = models.DateTimeField(auto_now_add=True)<br>

    WeatherMoments = models.Manager()<br>

    def __str__(self):<br>
        return self.date


<h2>Read</h2>[Story 3: Display all items from database],[Story 4: Details page]



<h2>Update and Delete</h2>[Story 5: Edit and Delete Functions]

<h2>Web Scraping</h2>[Stories 6 & 7: Beautiful Soup],[Story 9: Save API or scraped results]

<h2>API</h2>[Stories 6 & 7: API],[Story 9: Save API or scraped results]

<h2>Front End Development</h2>[Story 8: Front End Improvements]

<h2>Skills Acquired</h2>
This was a fun and challenging project for me. I learned a lot of great back and front-end skills that I will implement in the future. There are still more designing and features I would like to add to this project.
