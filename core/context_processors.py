def menu_context(request):
    """
    Контекстный процессор для передачи данных меню во все шаблоны
    """
    context = {
        'site_name': 'Барбершоп "Hard Rock"',
        'current_year': 2025,
        'menu_items': [
            {'name': 'О нас', 'url': '#about', 'anchor': True},
            {'name': 'Услуги', 'url': '#services', 'anchor': True},
            {'name': 'Мастера', 'url': '#masters', 'anchor': True},
            {'name': 'Запись', 'url': '#booking', 'anchor': True},
        ]
    }
    
    # Добавляем пункты меню для staff пользователей
    if request.user.is_authenticated and request.user.is_staff:
        context['staff_menu_items'] = [
            {'name': 'Заявки', 'url': 'orders_list', 'icon': 'bi-list-ul'},
        ]
    
    return context