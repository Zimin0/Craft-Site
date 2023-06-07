from django.shortcuts import render, redirect
from mainApp.models import Product, Unit
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from mainApp.models import Product


def index_view(request):
    products = Product.objects.all().select_related('unit')
    return render(request, 'mainApp/index.html', {'products': products})


def add_product_view(request):
    units = Unit.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        unit_id = request.POST.get('unit')
        unit = Unit.objects.get(id=unit_id)
        if Product.objects.filter(name=name).exists():
            return render(request, 'mainApp/add_product.html', {'error': 'Такой товар уже существует', 'units': units})
        else:
            product = Product(name=name, unit=unit)
            product.save()
            return redirect('index')
    return render(request, 'mainApp/add_product.html', {'units': units})

@require_GET
def search_products(request):
    search_query = request.GET.get('query', '')  # Получаем значение поискового запроса из параметра 'query'

    # Выполняем поиск товаров на основе поискового запроса
    products = Product.objects.filter(name__icontains=search_query.lower())

    # Создаем список словарей с данными о найденных товарах
    products_data = [{'name': product.name, 'quantity': product.get_quantity(), 'last_updated':product.get_datetime(), 'unit':product.unit.get_slug()} for product in products]
    return JsonResponse({'products': products_data})


def delete_product_view(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(pk=product_id)
        product.delete()
        return JsonResponse({'message': 'Товар успешно удален.'})
    return JsonResponse({'error': 'Ошибка удаления товара.'})

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_quantity_view(request, product_id):
    if request.method == 'POST':
        quantity = float(request.POST.get('quantity', 0))
        if quantity > 0:
            product = Product.objects.get(pk=product_id)
            product.quantity += quantity
            product.save()

            # Получение значения единицы измерения
            unit_name = product.unit.get_slug()

            # Возвращение нового значения количества и единицы измерения в формате JSON
            response_data = {
                'quantity': product.quantity,
                'unit': unit_name
            }
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Количество должно быть положительным числом.'})
    else:
        return JsonResponse({'error': 'Недопустимый метод запроса.'})
