from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None, user=None):
        self.text = text 
        self.timestamp = timestamp
        self.user = user
        
    #do my subclasses automatically inheret this?     
    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    #why do i need to reinitialize when TextPost inherits
    #the objects attributes from Post? 
    def __init__(self, text, timestamp=None):
        super().__init__(text, timestamp)
       
    def __str__(self):
        return '@{} {}: "{}"\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.timestamp.strftime("%A, %b %d, %Y"))


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        self.image_url = image_url
        super().__init__(text, timestamp)
        

    def __str__(self):
        return '@{} {}: "{}"\n\t{}\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.image_url, self.timestamp.strftime("%A, %b %d, %Y"))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.latitude = latitude
        self.longitude = longitude 
        super().__init__(text, timestamp)

    def __str__(self):
        return '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.user.first_name, self.text, self.latitude, self.longitude, self.timestamp.strftime("%A, %b %d, %Y"))
