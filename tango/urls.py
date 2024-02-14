from django.urls import path
from . import views
from .forms import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.About,name='about'),
    path('course/<str:slug>/',views.Courses,name='course'),
    path('contact/',views.Contact,name='contact'),
    path('support/',views.Help,name='help'),
    path('blog/',views.Articles,name='newsletter'),
    path('news/',views.News,name='news'),
    path('profile/',views.Profile,name='profile'),
    path('update-profile/<str:slug>/',views.UpdateProfile,name='update-profile'),
    path('complete_course/',views.CompleteCourse,name='complete_course'),
    path('certificate/',views.Certificate,name='certificate'),
    
    path('payment/<str:slug>/',views.PaymentPage,name='payment'),
    path('verify_payment/', views.verifyPayment , name = 'verify_payment'),
    path('adminPage/',views.adminPage,name='adminpage'),
  
    path('reset_password/',views.CustomPasswordResetView.as_view(),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="tango/reset_password_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="tango/reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="tango/reset_password_done.html"),name="password_reset_complete"),

    path('login/',views.LoginPage,name='loginpage'),
    path('register/',views.Register,name='register'),
    path('logout/',views.LogoutPage,name='logoutpage'),

    path('terms_and_conditions/',views.TermsCondition,name='term_condition'),
    path('refund_policy/',views.ReturnPolicy,name='return_policy'),
    path('privacy_policy/',views.PrivacyPolicy,name='privacy_policy'),
    path('testimonial_policy/',views.TestimonialPolicy,name='testimonial_policy'),

    # path('playlist/<str:slug>/',views.playlist,name='playlist'),
    path('watch/<str:slug>/<int:pk>/',views.watch,name='watch'),

    path('videopage/',views.VideoPage,name='videopage'),
    path('createvideopage/',views.CreateVideoPage,name='createvideopage'),
    path('updatevideopage/<int:pk>/',views.UpdateVideoPage,name='updatevideopage'),
    path('deletvideoepage/<int:pk>/',views.DeleteVideoPage,name='deletevideopage'),

    path('coursepage/',views.CoursePage,name='coursepage'),
    path('createcoursepage/',views.CreateCoursePage,name='createcoursepage'),
    path('updatecoursepage/<int:pk>/',views.UpdateCoursePage,name='updatecoursepage'),
    path('deletecoursepage/<int:pk>/',views.DeleteCoursePage,name='deletecoursepage'),

    path('chapterpage/',views.ChapterPage,name='chapterpage'),
    path('createchapterpage/',views.CreateChapterPage,name='createchapterpage'),
    path('updatechapterpage/<int:pk>/',views.UpdateChapterPage,name='updatechapterpage'),
    path('deletechapterpage/<int:pk>/',views.DeleteChapterPage,name='deletechapterpage'),

    path('userpage/',views.UserPage,name='userpage'),
    path('deleteuserpage/<int:pk>/',views.DeleteUserPage,name='deleteuserpage'),

    path('couponpage/',views.CouponPage,name='couponpage'),
    path('createcouponpage/',views.CreateCouponPage,name='createcouponpage'),
    path('updatecouponpage/<int:pk>/',views.UpdateCouponPage,name='updatecouponpage'),
    path('deletecouponpage/<int:pk>/',views.DeleteCouponPage,name='deletecouponpage'),

    path('profilepage/',views.ProfilePage,name='profilepage'),
    path('deleteprofilepage/<int:pk>/',views.DeleteProfilePage,name='deleteprofilepage'),

    path('couponuserpage/',views.CouponUserPage,name='couponuserpage'),

    path('quiz/<str:cor>/<str:ch>/',views.Quiz,name='quiz'),
    path('quiz_score/<str:cor>/<str:ch>/<int:score>/<str:wrong_ans>/',views.QuizScore,name='quiz_score'),
]
