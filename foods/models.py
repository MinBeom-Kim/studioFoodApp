from django.db import models
from users import models as users_models
from django.utils import timezone

class Food(models.Model):

    """ Food Model """

    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    one_supply = models.FloatField(default=0)
    unit = models.CharField(max_length=10, default='g')
    total_supply = models.FloatField(default=0)
    kcal = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    carbohydrate = models.FloatField(default=0)
    fat = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Diet(models.Model):
    def title(self):
        pass
    def kcal(self):
        pass
    def protein(self):
        pass
    def carbohydrate(self):
        pass
    def fat(self):
        pass
    def eaten(self):
        pass
    
    
    title = models.CharField(max_length=100, default=title)
    user_name = models.ForeignKey(users_models.User, on_delete=models.CASCADE, null=True, blank=True)

    menu1 = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True, related_name="diet_munu1")
    menu2 = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True, related_name="diet_munu2")
    menu3 = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True, related_name="diet_munu3")
    menu4 = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True, related_name="diet_munu4")
    menu5 = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True, related_name="diet_munu5")

    food = models.ManyToManyField(Food, related_name="diets", blank=True)
    start_at = models.DateTimeField(null = True)
    end_at = models.DateTimeField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(blank = True, null = True)

    before_menu1 = models.FloatField(default=0)
    before_menu2 = models.FloatField(default=0)
    before_menu3 = models.FloatField(default=0)
    before_menu4 = models.FloatField(default=0)
    before_menu5 = models.FloatField(default=0)

    after_menu1 = models.FloatField(default=0)
    after_menu2 = models.FloatField(default=0)
    after_menu3 = models.FloatField(default=0)
    after_menu4 = models.FloatField(default=0)
    after_menu5 = models.FloatField(default=0)

    eaten = models.FloatField(default=0)
    eaten_menu1 = models.FloatField(default=0)
    eaten_menu2 = models.FloatField(default=0)
    eaten_menu3 = models.FloatField(default=0)
    eaten_menu4 = models.FloatField(default=0)
    eaten_menu5 = models.FloatField(default=0)


    kcal = models.FloatField(null=True)
    protein = models.FloatField(null=True)
    carbohydrate = models.FloatField(null=True)
    fat = models.FloatField(null=True)


    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def title(self):
        self.title = str(self.start_at) + '먹은' + str(self.user_name) + '의 식단'
        return self.title

    def eaten(self):
        self.eaten_menu1 = self.before_menu1 - self.after_menu1

        self.eaten_menu2 = self.before_menu2 - self.after_menu2

        self.eaten_menu3 = self.before_menu3 - self.after_menu3

        self.eaten_menu4 = self.before_menu4 - self.after_menu4
        self.eaten_menu5 = self.before_menu5 - self.after_menu5
        self.save()

    def nutrition(self):
        self.eaten()
        
        try:
            # menu1
            one_supply = self.menu1.one_supply

            kcal = self.menu1.kcal / one_supply
            protein = self.menu1.protein / one_supply
            carbohydrate = self.menu1.carbohydrate / one_supply
            fat = self.menu1.fat / one_supply

            nutrition_kcal = self.eaten_menu1 * kcal

            nutrition_protein = self.eaten_menu1 * protein

            nutrition_carbohydrate = self.eaten_menu1 * carbohydrate

            nutrition_fat = self.eaten_menu1 *  fat
            
            self.kcal = nutrition_kcal
            self.protein = nutrition_protein
            self.carbohydrate = nutrition_carbohydrate
            self.fat = nutrition_fat

            # menu2
            one_supply = self.menu2.one_supply

            kcal = self.menu2.kcal / one_supply
            protein = self.menu2.protein / one_supply
            carbohydrate = self.menu2.carbohydrate / one_supply
            fat = self.menu2.fat / one_supply

            nutrition_kcal = self.eaten_menu2 * kcal

            nutrition_protein = self.eaten_menu2 * protein

            nutrition_carbohydrate = self.eaten_menu2 * carbohydrate

            nutrition_fat = self.eaten_menu2 *  fat

            self.kcal += nutrition_kcal
            self.protein += nutrition_protein
            self.carbohydrate += nutrition_carbohydrate
            self.fat += nutrition_fat

            # menu3
            one_supply = self.menu3.one_supply

            kcal = self.menu3.kcal / one_supply
            protein = self.menu3.protein / one_supply
            carbohydrate = self.menu3.carbohydrate / one_supply
            fat = self.menu3.fat / one_supply

            nutrition_kcal = self.eaten_menu3 * kcal

            nutrition_protein = self.eaten_menu3 * protein

            nutrition_carbohydrate = self.eaten_menu3 * carbohydrate

            nutrition_fat = self.eaten_menu3 *  fat

            self.kcal += nutrition_kcal
            self.protein += nutrition_protein
            self.carbohydrate += nutrition_carbohydrate
            self.fat += nutrition_fat

            # menu4
            one_supply = self.menu4.one_supply

            kcal = self.menu4.kcal / one_supply
            protein = self.menu4.protein / one_supply
            carbohydrate = self.menu4.carbohydrate / one_supply
            fat = self.menu4.fat / one_supply

            nutrition_kcal = self.eaten_menu4 * kcal

            nutrition_protein = self.eaten_menu4 * protein

            nutrition_carbohydrate = self.eaten_menu4 * carbohydrate

            nutrition_fat = self.eaten_menu4 *  fat

            self.kcal += nutrition_kcal
            self.protein += nutrition_protein
            self.carbohydrate += nutrition_carbohydrate
            self.fat += nutrition_fat

            # menu5
            one_supply = self.menu5.one_supply

            kcal = self.menu5.kcal / one_supply
            protein = self.menu5.protein / one_supply
            carbohydrate = self.menu5.carbohydrate / one_supply
            fat = self.menu5.fat / one_supply

            nutrition_kcal = self.eaten_menu5 * kcal

            nutrition_protein = self.eaten_menu5 * protein

            nutrition_carbohydrate = self.eaten_menu5 * carbohydrate

            nutrition_fat = self.eaten_menu5 *  fat

            self.kcal += nutrition_kcal
            self.protein += nutrition_protein
            self.carbohydrate += nutrition_carbohydrate
            self.fat += nutrition_fat


        except:
            pass

    
    def kcal(self):
        self.nutrition()
        return self.kcal

    def protein(self):
        self.nutrition()
        self.protein = self.menu1.protein
        return self.protein

    def carbohydrate(self):
        self.nutrition()
        self.carbohydrate = self.menu1.carbohydrate
        return self.carbohydrate

    def fat(self):
        self.nutrition()
        self.fat = self.menu1.fat
        return self.fat

    def __str__(self):
        self.eaten()
        title = str(self.start_at) + '먹은' + str(self.user_name) + '의 식단'
        return title

    