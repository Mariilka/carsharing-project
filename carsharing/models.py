from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Класс авто")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cars', verbose_name="Категория")
    brand = models.CharField(max_length=50, verbose_name="Марка")
    model = models.CharField(max_length=50, verbose_name="Модель")
    plate_number = models.CharField(max_length=15, unique=True, verbose_name="Гос. номер")
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена за сутки")

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.plate_number})"


class Client(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    driver_license = models.CharField(max_length=20, unique=True, verbose_name="ВУ (Права)")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rentals', verbose_name="Автомобиль")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='rentals', verbose_name="Клиент")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Итоговая сумма")

    class Meta:
        verbose_name = "Аренда"
        verbose_name_plural = "Аренды"

    def __str__(self):
        return f"Аренда #{self.id} — {self.car.brand} ({self.client.last_name})"


class Payment(models.Model):
    rental = models.OneToOneField(Rental, on_delete=models.CASCADE, related_name='payment', verbose_name="Аренда")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма оплаты")
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты")

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"Оплата #{self.id} (Аренда #{self.rental.id})"