# Daily Progress #

Below is the progress done by @ryanegbert each day on YadaYada Now.

###Wednesday, June 24###


### Tuesday, June 23 (2hr)###
* Research into Flask
* Initialized Flask project

### Monday, June 22 (1hr)###
* Finished setting up repo
* More research into [Flask](https://flask.palletsprojects.com/en/1.1.x/) vs [Django](https://www.djangoproject.com/)

Notes:
([Here](https://testdriven.io/blog/django-vs-flask/) is a website that helped with the comparison.)

Important questions to ask:
* What data will we store in our database?
  * Address to Youtube video
  * Topic / Subject
  * ICD10 Code / Id for subject (for non-medical questions)
  * Name (?)
  * Description (?)
  * Keywords (?)
  * Doc (?)

* Do we prefer relational vs. non-relational database? (MySQL vs Mongo)

My initial thoughts are that a SQL database will be much quicker to use in terms of read/write time.  For our searches, that could come in handy.  However, Flask sounds more appealing and would in turn work better with a non-relational database.  Searches would be slower, but development/maintenance would be quicker.

**Tentative plan: Flask framework w/ SQL database**