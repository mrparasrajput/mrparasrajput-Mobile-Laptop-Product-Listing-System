from .models import Cart

def cart_count(request):
    count = 0
    try:
        if request.session.session_key:
            cart = Cart.objects.filter(
                session_key=request.session.session_key
            ).first()
            if cart:
                count = cart.get_total_items()
    except:
        pass
    return {'cart_item_count': count}