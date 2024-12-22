class Intro:
    def __init__(self, obj):
        self.obj = obj

obj1 = Intro(42)

def introspection_info(obj):
    # Получаем объект, который хранится в obj1
    obj_data = obj.obj
    type_obj = type(obj_data)
    module_obj = obj1.__module__
    # Получаем атрибуты объекта (например, числового типа int)
    attributes = [attr for attr in dir(obj_data) if not callable(getattr(obj_data, attr))]
    # Получаем методы объекта (например, методы для int)
    methods = [method for method in dir(obj_data) if callable(getattr(obj_data, method))]
    dict_intro = {
        "type": type_obj,
        "attributes": attributes,
        "methods": methods,
        "module": module_obj
    }
    return dict_intro

print(introspection_info(obj1))