from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *
from django.contrib.auth.models import User


class UserStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'Address',
                  'Phone_number', 'Profile_picture', 'Bio', 'Student_No', 'Gender', 'Date_of_Birth',
                  'Nationality']
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        user = Student.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'Phone_number',
                  'Linkedin', 'Languages', 'Hobbies', 'Profile_picture', 'Teacher_Profile',
                  'Experience', 'Education', 'Skills']
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        user = Teachers.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()



class Online_Examination_SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Online_Examination_System
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields='__all__'

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=UserProfile
#         fields='__all__'


# class Meta:
#     model = UserProfile
#     fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age', 'phone_number', 'status']
#     extra_kwargs = {'password': {'write_only': True}}
#
# def create(self, validated_data):
#     user = UserProfile.objects.create_user(**validated_data)
#     return user


class StudentProSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']


class ExamProSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['exam_name']


class TeachersProSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['first_name']


class CourseProSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name']


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):
    user = StudentProSerializer()
    exam = ExamProSerializer()
    course = CoursesSerializer()

    class Meta:
        model = Questions
        fields = ['topic_name', 'user', 'course', 'exam', 'text', 'Option_A', 'Option_B',
                  'Option_C', 'correct_answer', 'correct_option']


class QuestionsProSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['text', 'Option_A', 'Option_B',
                  'Option_C', 'correct_answer']


class CourseSerializer(serializers.ModelSerializer):
    created_by = TeachersProSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['course_name', 'description', 'price', 'created_by',
                   'regis_date', 'updated_at', 'level', 'status']


class LessonSerializer(serializers.ModelSerializer):
    course = CoursesSerializer(many=True)
    lesson_date = serializers.DateTimeField(format='%d-%m-%Y  %H:%M')

    class Meta:
        model = Lesson
        fields = ['lesson_name', 'content', 'course', 'lesson_date']


class LessonVideoSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()
    lesson_data = serializers.DateTimeField(format='%d-%m-%Y  %H:%M')

    class Meta:
        model = LessonVideo
        fields = ['lesson', 'lesson_video', 'lesson_image', 'lesson_data']


class CourseVideoSerializer(serializers.ModelSerializer):
    course = CourseProSerializer()

    class Meta:
        model = CourseVideo
        fields = ['course', 'course_video', 'course_image', 'course_data']


class HomeworkSerializer(serializers.ModelSerializer):
    teacher = TeachersProSerializer()
    user = StudentProSerializer()
    due_date = serializers.DateTimeField(format='%d-%m-%Y  %H:%M')

    class Meta:
        model = Homework
        fields = ['topic_name', 'teacher', 'is_completed', 'user', 'description', 'due_date']


class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionsProSerializer(many=True, read_only=True)
    course = CoursesSerializer()
    teacher = TeachersProSerializer()
    exam_date = serializers.DateTimeField(format='%d-%m-%Y  %H:%M')

    class Meta:
        model = Exam
        fields = ['exam_name', 'course', 'teacher', 'exam_date', 'passing_score', 'duration', 'questions']


class CertificateSerializer(serializers.ModelSerializer):
    student = StudentProSerializer()
    course = CoursesSerializer()
    issued_at = serializers.DateField(format='%d-%m-%Y')
    expiry_date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = Certificate
        fields = ['student', 'course', 'issued_at', 'certificate_url', 'expiry_date']


class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    user = StudentProSerializer()
    favorite_course = CourseProSerializer()
    register_date = serializers.DateTimeField(format='%d-%m-%Y  %H:%M')

    class Meta:
        model = Favorite
        fields = ['user', 'favorite_course', 'register_date']


class CartSerializer(serializers.ModelSerializer):
    user = StudentProSerializer()

    class Meta:
        model = Cart
        fields = ['user']


class CarCourseSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    course = CourseProSerializer()

    class Meta:
        model = CarCourse
        fields = ['cart', 'course', 'quantity']


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['Phone_number', 'Linkedin', 'Languages', 'Hobbies',
                  'Profile_picture', 'Teacher_Profile', 'Experience', 'Education', 'Skills']

    # class Meta:
    #     model = Teachers
    #     fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age', 'phone_number', 'status']
    #     extra_kwargs = {'password': {'write_only': True}}
    #
    # def create(self, validated_data):
    #     teacher= Teachers.objects.create_user(**validated_data)
    #     return teacher


class StudentSerializer(serializers.ModelSerializer):
    Test_date = serializers.DateField(format='%d-%m-%Y')
    Date_of_Birth = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = Student
        fields = ['Address', 'Phone_number', 'Profile_picture', 'Bio', 'Test_date',
                  'Student_No', 'Gender', 'Date_of_Birth', 'Nationality']


class Teachers_ScheduleSerializer(serializers.ModelSerializer):
    teacher=TeachersProSerializer()
    class Meta:
        model = Teachers_Schedule
        fields = ['teacher','quality']


class SubscriptionSerializer(serializers.ModelSerializer):
    user = StudentProSerializer()
    courses = CourseProSerializer(many=True)
    start_date = serializers.DateTimeField(format='%d-%m-%Y  %H:%M')
    end_date = serializers.DateTimeField(format='%d-%m-%Y  %H:%M')

    class Meta:
        model = Subscription
        fields = ['user', 'start_date', 'end_date', 'active', 'courses']


class CoursePricingSerializer(serializers.ModelSerializer):
    course = CourseProSerializer()
    user = StudentProSerializer()
    payment_date = serializers.DateTimeField(format='%d-%m-%Y  %H:%M')

    class Meta:
        model = CoursePricing
        fields = ['course', 'user', 'price', 'payment_date', 'status']


class StudyGroupSerializer(serializers.ModelSerializer):
    members = StudentProSerializer()
    teachers = TeachersProSerializer()
    course = CourseProSerializer()
    study_at = serializers.DateTimeField(format='%d-%m-%Y  %H:%M')

    class Meta:
        model = StudyGroup
        fields = ['name', 'description', 'members', 'course', 'teachers', 'study_at']


class AttendanceSerializer(serializers.ModelSerializer):
    student = StudentProSerializer()
    lesson = LessonSerializer()
    attended_at = serializers.DateTimeField(format='%d-%m-%Y  %H:%M')

    class Meta:
        model = Attendance
        fields = ['student', 'lesson', 'attended_at', 'status']


class ExamResultSerializer(serializers.ModelSerializer):
    student = StudentProSerializer()
    exam = ExamProSerializer()
    graded_at = serializers.DateTimeField(format='%d-%m-%Y  %H:%M')

    class Meta:
        model = ExamResult
        fields = ['student', 'exam', 'score', 'passed', 'graded_at']
