from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

# from django.core.validators import MinValueValidator, MaxValueValidator


class Online_Examination_System(models.Model):
    instructions = models.CharField(max_length=500)


class UserProfile(AbstractUser):
    pass


class Student(UserProfile):
    Address = models.CharField(max_length=100)
    Phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    Profile_picture = models.ImageField(upload_to='user_images/')
    Bio = models.TextField()
    Test_date = models.DateTimeField(auto_now_add=True)
    Student_No = models.CharField(max_length=255, unique=True)
    Gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
                              null=True, blank=True)
    Date_of_Birth = models.DateField(null=True, blank=True)
    Nationality = models.CharField(max_length=50, null=True, blank=True)
    user_role = models.CharField(max_length=16, default='student')


    def __str__(self):
        return f'{self.first_name},{self.last_name} - {self.user_role}'


class Teachers(UserProfile):
    Phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    Linkedin = models.URLField()
    Languages = models.CharField(max_length=255)
    Hobbies = models.CharField(max_length=255, null=True, blank=True)
    Profile_picture = models.ImageField(upload_to='teachers_images/')
    Teacher_Profile = models.TextField()
    Experience = models.CharField(max_length=255)
    Education = models.CharField(max_length=255)
    Skills = models.CharField(max_length=500)
    user_role = models.CharField(max_length=16, default='teacher')

    def __str__(self):
        return f'{self.first_name},{self.last_name} - {self.user_role}'


class Teachers_Schedule(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='teacher_schedules', null=True,
                                blank=True)
    CHOICES_WORK_DAYS = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('wednesday', 'wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    quality = MultiSelectField(choices=CHOICES_WORK_DAYS)

    def __str__(self):
        return f'{self.teacher},{self.quality}'


class Course(models.Model):
    course_name = models.CharField(max_length=60, unique=True)
    description = models.TextField()
    price = models.PositiveSmallIntegerField()
    created_by = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='courses_created',null=True,blank=True)
    regis_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now_add=True,  null=True, blank=True)
    level = models.CharField(max_length=20, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'),
                                                     ('advanced', 'Advanced')])
    status = models.CharField(max_length=10, choices=[('free', 'Free'), ('premium', 'Premium')], default='free')

    def __str__(self):
        return f'{self.course_name},{self.level},{self.status}'


class Subscription(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE,null=True,blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f'Subscription for {self.user} , from {self.start_date} , to {self.end_date}'


# class Transaction(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_date = models.DateTimeField(auto_now_add=True)
#     payment_status = models.CharField(max_length=20, choices=[('completed', 'Completed'), ('failed', 'Failed')])

class CoursePricing(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(Student, on_delete=models.CASCADE,null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='unpaid')

    def __str__(self):
        return f'{self.user} , paid {self.price} , for {self.course}'


class CourseVideo(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_video')
    course_video = models.FileField(upload_to='course_video/')
    course_image = models.ImageField(upload_to='course_image/')
    course_data = models.DateTimeField(auto_now_add=True)


class StudyGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(Student, related_name='study_groups_enrolled')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='study_groups')
    teachers = models.ManyToManyField(Teachers, related_name='study_groups_taught')
    study_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.course}'


class Courses(models.Model):
    curses_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.curses_name}'


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=35)
    content = models.TextField()
    course = models.ManyToManyField(Courses, related_name='lessons')
    lesson_date = models.DateTimeField()

    def __str__(self):
        return f'{self.lesson_name},{self.course}'


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True,blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="attendances")
    attended_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('present', 'Present'), ('absent', 'Absent')])

    def __str__(self):
        return f'{self.student} , attended {self.lesson}'


#
# class LessonProgress(models.Model):
#     student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="lesson_progress")
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="progress")
#     is_completed = models.BooleanField(default=False)


class Homework(models.Model):
    topic_name = models.CharField(max_length=255)
    due_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='homeworks',null=True,blank=True)
    is_completed = models.BooleanField(default=False)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    description = models.TextField()  #second line

    # Monday=models.CharField(max_length=255)
    # Tuesday=models.CharField(max_length=255)
    # Wednesday=models.CharField(max_length=255)
    # Friday=models.CharField(max_length=255)
    # Saturday=models.CharField(max_length=255)


class LessonVideo(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lessons')
    lesson_video = models.FileField(upload_to='lesson_video/')
    lesson_image = models.ImageField(upload_to='lesson_image/')
    lesson_data = models.DateTimeField(auto_now_add=True)


class Exam(models.Model):
    exam_name = models.CharField(max_length=40)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='exams')
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, null=True, blank=True)
    exam_date = models.DateTimeField(auto_now_add=True)
    passing_score = models.PositiveSmallIntegerField(verbose_name='проходной балл')
    duration = models.DurationField(verbose_name='Время на выполнение')

    def __str__(self):
        return f'{self.exam_name} , {self.course}'


class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True,blank=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField()
    passed = models.BooleanField(default=False)
    graded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student} score {self.score} in {self.exam} - passed: {self.passed}'


class Questions(models.Model):
    topic_name = models.CharField(max_length=100)
    user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='questions',null=True,blank=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='questions')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    Option_A = models.CharField(max_length=255)
    Option_B = models.CharField(max_length=255)
    Option_C = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1, choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C')], )
    correct_option = models.CharField(max_length=1, choices=[("A", "Option A"), ("B", "Option B"), ("C", "Option C")],
                                      )

    def __str__(self):
        return f'{self.topic_name},{self.user},{self.course},{self.text}'


class Certificate(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate_url = models.FileField(verbose_name='сертификат', null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.student}, Certificate for {self.course}'


class CourseReview(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='course_reviews',null=True,blank=True)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='course_reviews_by_user',null=True,blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_reviews')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} , {self.course} , {self.rating}'


class Favorite(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='favorite_user')
    favorite_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    register_date = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f' {self.user}'


class CarCourse(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

# covered_skills=models.TextField()
#    # Камтылган көндүмдөр,Охватываемые навыки::
