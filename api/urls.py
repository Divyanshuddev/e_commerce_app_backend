from django.urls import path
from .views import get_user,sign_up_user,authentication,get_product,post_product,update_wish_list,count_likes,update_add_to_cart,count_cart,get_product_by_id,get_total_price,update_quantity,get_product_by_category,change_category

urlpatterns = [
    path('user/',get_user,name='get_user'),
    path('sign-up-user/',sign_up_user,name='sign_up_user'),
    path('login/',authentication,name='authentication'),
    path('get-products/',get_product,name='get_product'),
    path('post-product/',post_product,name='post_product'),
    path('wish-list/',update_wish_list,name='update_wish_list,name'),
    path('count-likes/',count_likes,name='count_likes'),
    path('update-cart/',update_add_to_cart,name='update_add_to_cart'),
    path('cart-data/',count_cart,name='count_cart'),
    path('product/<str:product_id>',get_product_by_id,name='get_product_by_id'),
    path('total-price/',get_total_price,name='get_total_price'),
    path('update-quantity/',update_quantity,name='update_quantity'),
    path('category/<str:type>',get_product_by_category,name="get_product_by_category"),
    path('change-category/<str:product_id>',change_category,name='change_category')
]
