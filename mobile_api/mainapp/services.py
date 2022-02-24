from .models import Shop


def check_user(phone: str, shop_id: int)-> bool:
    """
    Checks if user has access to shop
    """
    shop = Shop.objects.filter(
        id=shop_id,
        worker__phone=phone
        )
    if not shop:
        return False
    return True
    
    