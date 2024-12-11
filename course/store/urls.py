from django.urls import path,include
from .views import *
from rest_framework import routers
router=routers.DefaultRouter()


router.register(r'online',Online_Examination_SystemViewSet,basename='online_list')

router.register(r'user',UserProfileViewSet,basename='user_list')

router.register(r'student',StudentViewSet,basename='student_list')

router.register(r'questions',QuestionsViewSet,basename='questions_list')

router.register(r'courses',CoursesViewSet,basename='courses_list')

router.register(r'lesson',LessonViewSet,basename='lesson_list')

router.register(r'course_video',CourseVideoViewSet,basename='course_video_list')

router.register(r'lesson_video',LessonVideoViewSet,basename='lesson_video_list')

router.register(r'certificate',CertificateViewSet,basename='certificate_list')

router.register(r'favorite',FavoriteViewSet,basename='favorite_list')

router.register(r'cart',CartViewSet,basename='cart_list')

router.register(r'carcourse',CarCourseViewSet,basename='carcourse_list')

router.register(r'teacher',TeachersViewSet,basename='teacher_list')

router.register(r'teacher_schedule',Teachers_ScheduleViewSet,basename='teacher_schedule_list')

router.register(r'subscription',SubscriptionViewSet,basename='subscription_list')

router.register(r'course_pricing',CoursePricingViewSet,basename='course_pricing_list')

router.register(r'exam_result',ExamResultViewSet,basename='exam_result_list')

router.register(r'study_group',StudyGroupViewSet,basename='study_group_list')

router.register(r'attendance',AttendanceViewSet,basename='attendance_list')



urlpatterns=[
    path('',include(router.urls)),
    path('course/', CourseListViewSet.as_view(), name='course_list'),
    path('course/create/', CourseCreateViewSet.as_view(), name='course_create'),
    path('course/edit/<int:pk>/', CourseUpdateViewSet.as_view(), name='course_edit'),

    path('register_student/', RegisterStudentView.as_view(), name='register'),
    path('register_teacher/', RegisterTeacherView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('assignment/', HomeworkListViewSet.as_view(), name='assignment_list'),
    path('assignment/create/', HomeworkCreateViewSet.as_view({'post': 'create'}), name='assignment_create'),
    path('assignment/edit/<int:pk>/', HomeworkUpdateViewSet.as_view(), name='assignment_edit'),

    path('review/', CourseReviewListViewSet.as_view(), name='review_list'),
    path('review/create/', CourseReviewCreateViewSet.as_view(), name='review_create'),
    path('review/edit/<int:pk>/', CourseReviewUpdateViewSet.as_view(), name='review_edit'),

    path('exam/', ExamListViewSet.as_view(), name='exam_list'),
    path('exam/create/', ExamCreateViewSet.as_view(), name='exam_create'),
    path('exam/edit/<int:pk>/', ExamUpdateViewSet.as_view(), name='exam_edit'),
]