from django import template

register = template.Library()

# cart lgc
@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    for id in keys:
        if id == str(product.id):
            
            return True
    return False

@register.filter(name='cart_quantity')
def is_in_cart(Product,cart):
    keys = cart.keys()
    for id in keys:
        if id== str(Product.id):
            
            return cart.get(id)
    return 0