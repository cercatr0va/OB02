class User:
    """Класс, представляющий обычного сотрудника компании."""

    def __init__(self, user_id, name):
        self.__user_id = user_id  # Приватный атрибут
        self.__name = name  # Приватный атрибут
        self.__access_level = 'user'  # Приватный атрибут для уровня доступа

    # Метод для получения идентификатора пользователя
    def get_user_id(self):
        return self.__user_id

    # Метод для получения имени пользователя
    def get_name(self):
        return self.__name

    # Метод для получения уровня доступа пользователя
    def get_access_level(self):
        return self.__access_level

    # Метод для изменения имени пользователя
    def set_name(self, name):
        self.__name = name


class Admin(User):
    """Класс, представляющий администратора, наследуется от User."""

    def __init__(self, user_id, name):
        super().__init__(user_id, name)  # Вызов конструктора родительского класса
        self.__access_level = 'admin'  # Приватный атрибут для уровня доступа администратора

    # Метод для добавления пользователя
    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен администратором {self.get_name()}.")
        else:
            print("Ошибка: можно добавлять только объекты класса User.")

    # Метод для удаления пользователя
    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь с ID {user_id} удален администратором {self.get_name()}.")
                return
        print(f"Пользователь с ID {user_id} не найден.")


# Пример использования системы
if __name__ == "__main__":
    # Создание списка пользователей
    user_list = []

    # Создание обычных пользователей
    user1 = User(1, "Иван")
    user2 = User(2, "Елена")
    user3 = User(3, "Петр")

    # Добавляем пользователей в список
    user_list.append(user1)
    user_list.append(user2)

    # Вывод информации о пользователях
    for user in user_list:
        print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

    # Создание администратора
    admin = Admin(99, "Анна")

    # Администратор добавляет нового пользователя
    admin.add_user(user_list, user3)

    # Администратор удаляет пользователя по ID
    admin.remove_user(user_list, 2)

    # Вывод информации о пользователях после изменений
    print("\nОбновленный список пользователей:")
    for user in user_list:
        print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")
