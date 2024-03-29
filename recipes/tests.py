from django.test import TestCase
from .models import Recipe
from .forms import RecipeSearchForm

# Create your tests here.


class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(name="Coffee", cooking_time=5,
                              ingredients='Coffee Beans, Water, Sugar', description='test with some description')

    def test_name_max_lenght(self):
        recipe = Recipe.objects.get(id=1)
        name_max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(name_max_length, 120)

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        recipe_name_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(recipe_name_label, 'name')

    def test_cooking_time(self):
        recipe = Recipe.objects.get(id=1)
        recipe_cooking_time = recipe.cooking_time
        self.assertEqual(recipe_cooking_time, 5)

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/list/1')

    def test_calc_difficulty(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.calc_difficulty(), 'Easy')


class RecipesSearchFormTest(TestCase):
    def test_form_recipe_diff_input(self):
        form = RecipeSearchForm()
        self.assertIn('recipe_diff', form.as_p())

    def test_form_valid_data(self):
        form = RecipeSearchForm(
            data={'recipe_diff': '#1', 'chart_type': '#2'})
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = RecipeSearchForm(
            data={'recipe_diff': '', 'chart_type': ''})
        self.assertFalse(form.is_valid())
