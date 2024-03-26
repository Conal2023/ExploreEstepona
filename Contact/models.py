from django.db import models

select_mode_of_contact = (
    ("email","E-Mail"),
    ("phone","Phone"),
)
Select_question_categories = (
    ("post_a_blog", "Post A Blog"),
    ("issue_with_profile", "Issue With Profile"),
    ("recommendations", "Recommendations"),
    ("other", "Other"),
)

class Contact(models.Model):
    """ Model to structure the contact form"""
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    mode_of_contact = models.CharField('Contact by', 
    max_length=50,choices=select_mode_of_contact,default='email')
    question_categories = models.CharField('How are we able to help you?',
    max_length=50,choices=Select_question_categories,default='post_a_blog')
    message = models.TextField(max_length=3000)

    def __str__(self):
        return self.email
