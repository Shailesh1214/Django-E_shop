from django.shortcuts import render , redirect , HttpResponse
from store.models.product import Product
from store.models.category import Category
from django.views import View

# create your view here
class Index(View):
    def post(self, request):
        product =request.POST.get('product')
        cart =request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product]=1
        else:
            cart= {}
            cart[product]=1

        request.session['cart']=cart
        print(cart)
        return redirect('homepage')
    
    def get(self, request):
        products = None
        categories = Category.get_all_categories()
        categoryID = (request.GET.get('category'))
        if categoryID:
            products =Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products

        data = {}
        data['products'] = products
        data['categories'] = categories
        print('you are',request.session.get('email'))
        return render(request,'index.html', data)



    




        

