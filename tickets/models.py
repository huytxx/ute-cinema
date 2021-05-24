from django.db import models

# model đại diện cho vé xem phim
class Ticket(models.Model):
    name = models.CharField(max_length=1000) # tên của phim
    time = models.CharField(max_length=50) # thời gian chiếu
    release_time = models.CharField(max_length=50) # thời gian ra mắt
    description = models.TextField() # Thông tin phim
    type = models.CharField(max_length=1000) # kiểu phim, (2D, 3D...)
    fit_for = models.CharField(max_length=100) # lứa tuổi phù hợp
    image = models.ImageField(upload_to='picture') # ảnh của phim

    
    def __str__(self):
        return self.name

# Lớp đại diện cho slider list các phim sắp ra mắt ở phần header
class Carausel(models.Model):
    image = models.ImageField(upload_to='picture')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# list select cho các vé khuyến mãi
TYPE_CHOICES = {
    ('promotion','Promotion'),
    ('phim','Phim'),
    ('doi_tac','Đối tác'),
}

# lớp đại diện cho vé khuyến mãi
class Promotion(models.Model):
    title = models.CharField(max_length=150) # tên vé khuyến mãi
    image = models.ImageField(upload_to='picture') # ảnh vé khuyến mãi
    start_time = models.CharField(max_length=50) # thời gian bắt đầu khuyến mãi
    end_time = models.CharField(max_length=50) # thời gian kết thúc khuyến mãi
    type = models.CharField(max_length=90, choices=TYPE_CHOICES, default='promotion') # khuyến mãi phần gì

    def __str__(self):
        return self.title
    